from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

class ContentTypeRestrictedFileField(FileField):
    """
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file size allowed for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB 104857600
            250MB - 214958080
            500MB - 429916160
    """
    def __init__(self, *args, **kwargs):
        try:
            self.content_types = kwargs.pop("content_types")
        except KeyError:
            self.content_types = None

        try:
            self.file_extensions = kwargs.pop("file_extensions")
        except KeyError:
            self.file_extensions = None

        try:
            self.max_upload_size = kwargs.pop("max_upload_size")
        except KeyError:
            self.max_upload_size = None

        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)

        file = data.file
        try:
            # Check file extension if required
            if self.file_extensions:
                found = False
                for file_extension in self.file_extensions:
                    if file.name.endswith(".%s" % file_extension):
                        found = True
                        break

                if not found:
                    raise forms.ValidationError(_('File extension not supported.'))

            # Check content-type if required
            if self.content_types and file.content_type not in self.content_types:
                raise forms.ValidationError(_('Filetype not supported.'))

            # Check file size if required
            if self.max_upload_size and file._size > self.max_upload_size:
                raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (
                filesizeformat(self.max_upload_size), filesizeformat(file._size)))
        except AttributeError:
            pass

        return data