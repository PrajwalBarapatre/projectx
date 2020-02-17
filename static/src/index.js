// import './index.css';
// import App from './App';
// import * as serviceWorker from './serviceWorker';
const Router = window.ReactRouterDOM.BrowserRouter;
const Route =  window.ReactRouterDOM.Route;
const Link =  window.ReactRouterDOM.Link;
const Prompt =  window.ReactRouterDOM.Prompt;
const Switch = window.ReactRouterDOM.Switch;
const Redirect = window.ReactRouterDOM.Redirect;
const NavLink = window.ReactRouterDOM.NavLink;
// const Prompt = window.ReactRouterDOM.Prompt;
//Hoc
const Hoc = (props) => (
  props.children
);

//Base Router

const BaseRouter = () => (
    
      <Hoc>
    <Route exact path="/:chatID/" component={Chat} />
    </Hoc>
    
  
);


class Contact extends React.Component{
  constructor(props){
    super(props);

  }

  handleClick(){
    var chat_id = this.props.chat_id;
    var notif_id = this.props.notif_id;
    this.props.changeChat(chat_id, notif_id)
    //console.log('different chat clicked');
    //console.log('inside Contact');
  }
  
  render(){
    var number='';
    if(this.props.notif_number>0){
      number=''+this.props.notif_number;
    }else{
      number='';
    }
    return(
      <li className="contact" onClick={this.handleClick.bind(this)}  
      style={{ backgroundColor :  this.props.curr_chat==this.props.chat_id ? 'cornflowerblue' : 'rgba(0,0,0,0.3)' }}
      >
          <div className="wrap">
              <span className={`contact-status ${this.props.status}`}></span>
              <img src={this.props.picURL} alt="" />
              <div className="meta">
                  <p className="name">{this.props.name}     {number}</p>
                  
                  
                  {/* <p className="preview">You just got LITT up, Mike.</p> */}
              </div>
          </div>
      </li>
    )
  }

}

// const Contact = (props) => (
  
//       <li className="contact" onclick={this.handleClick.bind(this)}>
//           <div className="wrap">
//               <span className={`contact-status ${props.status}`}></span>
//               <img src={props.picURL} alt="" />
//               <div className="meta">
//                   <p className="name">{props.name}</p>
//                   {/* <p className="preview">You just got LITT up, Mike.</p> */}
//               </div>
//           </div>
//       </li>
      
  
// );
class WebSocketService {
    static instance = null;
    callbacks = {};
  
    static getInstance() {
      if (!WebSocketService.instance) {
        WebSocketService.instance = new WebSocketService();
      }
      return WebSocketService.instance;
    }
  
    constructor() {
      this.socketRef = null;
    }
  
    connect(chatUrl) {
      // const path = 'ws://www.bverge.com/ws/chat/test/';
      const path = `wss://www.bverge.com/ws/chat/${chatUrl}/`;
      this.socketRef = new WebSocket(path);
      this.socketRef.onopen = () => {
        //console.log('WebSocket open in '+ chatUrl);
      };
      this.socketNewMessage(JSON.stringify({
        command: 'fetch_messages'
      }));
      this.socketRef.onmessage = e => {
        //console.log('Message recieved on web socket');
        this.socketNewMessage(e.data);
      };
      this.socketRef.onerror = e => {
        //console.log(e.message);
      };
      this.socketRef.onclose = () => {
        //console.log("WebSocket closed let's reopen");
        
      };
    }

    disconnect(chat_id, notif_id){
      //console.log('last message');
      this.sendMessage({ command: 'change_chat', chat_id: chat_id, notif_id:notif_id });
      //console.log('closing the connection');

      this.socketRef.close()
      //console.log('connection closed');
    }
  
    socketNewMessage(data) {
      //console.log('Message recieved in socketNewMessage');
      const parsedData = JSON.parse(data);
      const command = parsedData.command;
      if (Object.keys(this.callbacks).length === 0) {
        return;
      }
      if (command === 'status'){
        this.callbacks[command](parsedData.status);
      }
      if (command === 'messages') {
        //console.log('command is messages');
        this.callbacks[command](parsedData.messages);
      }
      if (command === 'new_message') {
        //console.log('command is new_message');
        this.callbacks[command](parsedData.message);
      }
      if (command === 'blocked') {
        //console.log('command is blocked');
        this.callbacks[command]();
      }
      // if (command === 'new_notif') {
      //   //console.log('command is new_notif');
      //   this.callbacks[command](parsedData.message);
      // }
    }
  
    fetchMessages(username, chatId) {
      //console.log('sending message to fetch');
      this.sendMessage({ command: 'fetch_messages', username: username, chatId:chatId });
    }
  
    newChatMessage(message) {
      //console.log('sending message to new');
      this.sendMessage({ command: message.command, from: message.from, message: message.content, chatId: message.chat_id, malbum_id:message.malbum_id }); 
    }
  
    addCallbacks(messagesCallback, newMessageCallback, check_users, blockmessageCallback) {
      this.callbacks['messages'] = messagesCallback;
      this.callbacks['new_message'] = newMessageCallback;
      this.callbacks['status']=check_users;
      this.callbacks['blocked']=blockmessageCallback;
    }

    change_chat=(chat_id, notif_id)=>{
      this.sendMessage({ command: 'change_chat', chat_id: chat_id, notif_id:notif_id });
    }
    
    sendMessage(data) {
      try {
        //console.log('above send');
        this.socketRef.send(JSON.stringify({ ...data }));
        //console.log('message sent');
      }
      catch(err) {
        //console.log(err.message);
      }  
    }

    waitForSocketConnection(callback){
        const socket = this.socketRef;
        const recursion = this.waitForSocketConnection;
        setTimeout(
            function(){
                if(socket.readyState === 1){
                    //console.log('connection is secure');
                    if(callback != null){
                        callback();
                    }
                    return;
                }else{
                    //console.log('waiting for connection...');
                    recursion(callback); 
                }
            }, 1);
    }
  
    state() {
      return this.socketRef.readyState;
    }
  
  }
  
  const WebSocketInstance = WebSocketService.getInstance();

class Header extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      chats: [],
      other_profile_url: '',
      other_name : '',
      other_id : 0,
      blocked : 0,
    }
  }

  componentWillReceiveProps(props){
    
    this.setState({
      other_profile_url: props.other_profile_url,
      other_name : props.other_name,
      other_id : props.other_id,
      blocked : props.blocked
    })
  }

  clickBlock=()=>{
    //console.log('block clicked')
    this.props.renderBlock();
  }

  render(){
    var block_name = this.state.blocked==1 ? 'Unblock' : 'Block'
    var self_block = this.props.self_blocked==true ? '  Sorry, the user has blocked you' : ''
    return (
      <div className="contact-profile">
        <div className="profile_box">
          <img src={this.state.other_profile_url} alt="" />
          <p > {this.state.other_name} </p>
        </div>
        <p className="pl-4 bm-size f-w-bold  ff-pd"> <a href="/" class="c-3f"> Business Verge</a> </p>
        <div className="social-media">
          <button className="submit btn btn-block-unblock" onClick={this.clickBlock.bind(this)} >
            <h5>{block_name}</h5>
          </button>
        </div>
      </div>
    )
  }

}

class Sidepanel extends React.Component{

  constructor(props){
    super(props);
    this.state = {
      chats: [],
      other_profile_url: '',
      other_name : '',
      other_id : 0,
      blocked : 0,
    }
  }

  componentWillReceiveProps(props){
    this.getUserChats(props.username);
  }

  
  getUserChats = (username) => {
    //console.log(username);
    fetch(`https://www.bverge.com/chat/api/${username}`,{
            method: 'GET',
            headers: {
                 Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            // body: JSON.stringify({
            //     from_name:name
            // }),
        })
        .then((response)=>response.json())
        .then((responseJson)=>{
            //console.log(responseJson);
            // //console.log(responseJson.username);
            var blocked=0;
            if(responseJson.curr.blocked){
              blocked=1;
            }
            this.setState({
                chats:responseJson.chats,
                other_profile_url: 'https://bverge.s3.ap-south-1.amazonaws.com/'+responseJson.curr.other_profile_url,
                other_name : responseJson.curr.other_name,
                other_id : responseJson.curr.other_id,
                blocked : blocked
            });
            // //console.log("fetched")
            // ToastAndroid.showWithGravityAndOffset(
            //     "fetching",
            //     ToastAndroid.SHORT,
            //     ToastAndroid.TOP,
            //     0,
            //     40);
            
        });
        //console.log(username);
}


handleClick=(chat_id, notif_id)=>{
  this.props.handleContact(chat_id, notif_id)
  //console.log('inside Sidepanel');
}

  render(){

    const activeChats = this.state.chats.map(c => {
      var title, person='';
      var url = '';
      var status='';
      for(var i=0; i<c.people.length; i++){
        if(c.people[i].username!=this.props.username){
             person = c.people[i].username;
             url = c.people[i].url;
             status = c.people[i].status;
        }
      }
      title = c.business_name + '-' + person;
      var photo = 'https://bverge.s3.ap-south-1.amazonaws.com/'+url;
      return (
          <Contact 
              key={c.chat_id}
              chat_id = {c.chat_id}
              notif_id = {c.notif_id}
              notif_number = {c.notif_number}
              curr_chat = {this.props.curr_chat}
              name={title} 
              picURL={photo}
              status={status}
              changeChat={this.handleClick}
              chatURL={`${c.chat_id}`} />
      )
  })
    return(
      <div id="sidepanel">
      <div id="profile">
        <div className="wrap">
          <img id="profile-img" src={this.props.photo} className="online" alt="" />
          <p>{this.props.full_name}</p>
          {/* <i className="fa fa-chevron-down expand-button" aria-hidden="true"></i>
          <div id="status-options">
            <ul>
              <li id="status-online" className="active"><span className="status-circle"></span> <p>Online</p></li>
              <li id="status-away"><span className="status-circle"></span> <p>Away</p></li>
              <li id="status-busy"><span className="status-circle"></span> <p>Busy</p></li>
              <li id="status-offline"><span className="status-circle"></span> <p>Offline</p></li>
            </ul>
          </div> */}
          <div id="expanded">
            {/* <label htmlFor="twitter"><i className="fa fa-facebook fa-fw" aria-hidden="true"></i></label>
            <input name="twitter" type="text" value="mikeross" />
            <label htmlFor="twitter"><i className="fa fa-twitter fa-fw" aria-hidden="true"></i></label>
            <input name="twitter" type="text" value="ross81" />
            <label htmlFor="twitter"><i className="fa fa-instagram fa-fw" aria-hidden="true"></i></label>
            <input name="twitter" type="text" value="mike.ross" /> */}
          </div>
        </div>
      </div>
      {/* <div id="search">
        <label htmlFor=""><i className="fa fa-search" aria-hidden="true"></i></label>
        <input type="text" placeholder="Search contacts..." />
      </div> */}
      <div id="contacts">
        <ul>
        {activeChats}
          {/* <li className="contact">
            <div className="wrap">
              <span className="contact-status online"></span>
              <img src="http://emilcarlsson.se/assets/louislitt.png" alt="" />
              <div className="meta">
                <p className="name">Louis Litt</p>
                <p className="preview">You just got LITT up, Mike.</p>
              </div>
            </div>
          </li>
          <li className="contact active">
            <div className="wrap">
              <span className="contact-status busy"></span>
              <img src="http://emilcarlsson.se/assets/harveyspecter.png" alt="" />
              <div className="meta">
                <p className="name">Harvey Specter</p>
                <p className="preview">Wrong. You take the gun, or you pull out a bigger one. Or, you call their bluff. Or, you do any one of a hundred and htmlForty six other things.</p>
              </div>
            </div>
          </li> */}
        </ul>
      </div>
      
    </div>
    )
  }

}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function pdf_view(file_name){
  //console.log(file_name)
  fetch(`https://www.bverge.com/chat/pdf_view/${file_name}`,{
    method: 'GET'
  })
}

class Chat extends React.Component{


    initialiseChat(){
      //console.log(this.state)
      this.waitForSocketConnection(() => {
        WebSocketInstance.addCallbacks(this.setMessages.bind(this), this.addMessage.bind(this), this.check_users.bind(this), this.blockMessage.bind(this))
        WebSocketInstance.fetchMessages(
          this.state.currentUser,
          this.state.chatId);
      });
      var chatUrl = this.state.chatId;
      WebSocketInstance.connect(chatUrl);
    }

    constructor(props) {
        super(props);
        this.state = {
          currentUser:'',
          full_name:'',
          profile_url:'',
          chatId : 1,
          notif_id:1,
          message:'',
          messages:[],
          uploading : false,
          other_profile_url: '',
          other_name : '',
          blocked : 0,
          other_id: '',
          chats:[],
          self_blocked:false,
        }
        //console.log('this is chat');

        
        this.messageChangHandler = this.messageChangHandler.bind(this);
        this. sendMessageHandler = this.sendMessageHandler.bind(this);

        //console.log(props);
        }

    // componentWillReceiveProps(props){
    //   //console.log(props);
    //   this.initialiseChat();
    // }

    componentDidMount(){
      //console.log('inside didMount of chat');
      fetch('https://www.bverge.com/get_user',{
            method: 'GET',
            headers: {
                 Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            // body: JSON.stringify({
            //     from_name:name
            // }),
        })
        .then((response)=>response.json())
        .then((responseJson)=>{
            //console.log(responseJson);
            //console.log(responseJson.username);
            var fullname = responseJson.first_name + responseJson.last_name;
            var url = 'https://bverge.s3.ap-south-1.amazonaws.com/'+responseJson.photo_name ;
            //console.log(responseJson.curr_chat)
            var blocked=0;
            if(responseJson.blocked){
              blocked=1;
            }
            this.setState({
                currentUser:responseJson.username,
                profile_url : url,
                full_name : fullname,
                chatId: responseJson.curr_chat,
                notif_id: responseJson.notify_id,
                other_profile_url: 'https://bverge.s3.ap-south-1.amazonaws.com/'+responseJson.other_profile_url,
                other_name : responseJson.other_name,
                other_id : responseJson.other_id,
                blocked : blocked,
                chats:responseJson.chats
            },this.initialiseChat());
            // //console.log("fetched")
            // ToastAndroid.showWithGravityAndOffset(
            //     "fetching",
            //     ToastAndroid.SHORT,
            //     ToastAndroid.TOP,
            //     0,
            //     40);
            
        })
        this.scrollToBottom();

        
    }

    waitForSocketConnection(callback) {
        const component = this;
        setTimeout(
            function () {
            if (WebSocketInstance.state() === 1) {
                //console.log("Connection is made")
                callback();
                return;
            } else {
                //console.log("wait for connection...")
                component.waitForSocketConnection(callback);
            }
        }, 100);
    }
    
    addMessage(message) {
      //console.log('adding message to'+this.state.chatId);
        this.setState({ messages: [...this.state.messages, message], self_blocked:false});
        
    }
    
    setMessages(messages) {
      //console.log('adding messagess to'+this.state.chatId);
        this.setState({ messages: messages.reverse()});
    }

    check_users(status){
      this.setState({
        status:status
      });
    }

    renderTimestamp = timestamp => {
      let prefix = ''; 
      const timeDiff = Math.round((new Date().getTime() - new Date(timestamp).getTime())/60000);
      if (timeDiff < 1) { // less than one minute ago
          prefix = 'just now...';
      } else if (timeDiff < 60 && timeDiff >= 1) { // less than sixty minutes ago
          prefix = `${timeDiff} minutes ago`;
      } else if (timeDiff < 24*60 && timeDiff >= 60) { // less than 24 hours ago
          prefix = `${Math.round(timeDiff/60)} hours ago`;
      } else if (timeDiff < 31*24*60 && timeDiff >= 24*60) { // less than 7 days ago
          prefix = `${Math.round(timeDiff/(60*24))} days ago`;
      } else {
          prefix = `${new Date(timestamp)}`;
      }
      return prefix
  }

  blockMessage=()=>{
    this.setState({
      self_blocked:true
    })
  }

  


  renderMessage=(message)=>{
    var currentUser = this.state.currentUser;
    //console.log(message.file_exist)
    if(!message.file_exist){
      return (
            <li
                key = {message.id}
                className = {message.author == currentUser ? 'sent': 'replies'}
                style={{ display:  message.chat_id == this.state.chatId ? 'block' : 'none' }}>
            {/* <img src="http://emilcarlsson.se/assets/mikeross.png" /> */}
            
            
            <p>
            <h4>{message.author}</h4>
                {message.content}
                <br />
                <small>
                  {this.renderTimestamp(message.timestamp)}
                </small>
            </p>
            </li>
      )
    }else{
      var url = 'https://bverge.s3.ap-south-1.amazonaws.com/'+ message.content;
      var content = ''+message.content;
      var file_name = content
      content=content.replace('message/','');
      //console.log(content)
      return(
            <li
                key = {message.id}
                className = {message.author == currentUser ? 'sent': 'replies'}
                style={{ display:  message.chat_id == this.state.chatId ? 'block' : 'none' }}>
            {/* <img src="http://emilcarlsson.se/assets/mikeross.png" /> */}
            
            
            
            <p>
            <h4>{message.author}</h4>
            <a href={url}><i className="fa fa-download" aria-hidden="true"></i></a>
                {content}
                <br />

                <small>
                  {this.renderTimestamp(message.timestamp)}
                </small>
            </p>
            </li>
      )
    }
  }

    renderMessages = (messages)=>{
      //console.log('rendering message to'+ this.state.chatId);
      
        // const currentUser = 'minu1';
        var currentUser = this.state.currentUser;
        return messages.map(message => (
            this.renderMessage(message)
        ));
    }

    scrollToBottom = () => {
          this.messagesEnd.scrollIntoView({ behavior: "smooth" });
      }

    componentDidUpdate() {
        this.scrollToBottom();
    }

    changingConnection(){
      //console.log('chatId is set');
      //console.log(this.state)
      // WebSocketInstance.change_chat(this.state.chatId);
      WebSocketInstance.disconnect(this.state.chatId, this.state.notif_id);
      //console.log('Chat says websocket disconnected');
      this.waitForSocketConnection(() => {
        WebSocketInstance.fetchMessages(
          this.state.currentUser,
          this.state.chatId);
      });
      var chatUrl = this.state.chatId;
      //console.log(chatUrl);
      WebSocketInstance.connect(chatUrl);
      //console.log('new connection made');
    }

    sendMessageHandler = e =>{
        e.preventDefault();
        const messageObject = {
            from:this.state.currentUser,
            content:this.state.message,
            chat_id:this.state.chatId,
            command:'new_message'
        }
        //console.log('message objeect created in'+this.state.chatId);
        WebSocketInstance.newChatMessage(messageObject);
        //console.log('message objeect sent to newChatMessage in'+this.state.chatId);
        this.setState({
            message:''
        });
    }

    messageChangHandler = event =>{
        this.setState({
            message:event.target.value
        })
    }

    renderChat = (chat_id,notif_id) => {
      //console.log('inside renderChat')
        var arr = this.state.chats;
        var chatId=chat_id;
        var blocked_;
        for(var i=0; i<arr.length;i++){
          if(arr[i].chat_id==chatId){
           blocked_ = arr[i].blocked!='' ? 1 :0
           //console.log('/media/'+arr[i].other_profile_url)
           //console.log(arr[i].other_name)
           //console.log()
            this.setState({
              chatId : chat_id,
              notif_id:notif_id,
              other_profile_url:'https://bverge.s3.ap-south-1.amazonaws.com/'+arr[i].other_profile_url,
              other_name:arr[i].other_name,
              other_id:arr[i].other_id,
              blocked:blocked_,
              self_blocked:false
              
            }, this.changingConnection);
          }
        }
        //console.log(this.state)
        
      //console.log('chatId is going to set');
      
      
    }

    file_submit = e =>{
      const files = Array.from(e.target.files)
      this.setState({ uploading: true })

      files.forEach((file, i) => {
        var formData = new FormData()
        formData.append('file', file)
        formData.append('chat_id', this.state.chatId)
        formData.append('csrfmiddlewaretoken', getCookie('csrftoken'))
        fetch('upload_files',{
            method: 'POST',
            body: formData
        }).then((response)=>response.json())
        .then((responseJson)=>{

          //console.log(responseJson);
          // var data = responseJson.parse();
          // //console.log(data)
          var messageObject = {
            from:this.state.currentUser,
            chat_id:this.state.chatId,
            malbum_id:responseJson.malbum_id,
            command:'new_file'
          }
          //console.log('message objeect created in'+this.state.chatId);
          WebSocketInstance.newChatMessage(messageObject);
          //console.log('message objeect sent to newChatMessage in'+this.state.chatId);
        })
      })
    }

    handleBlock=()=>{
      //console.log('inside chat for block click')
      var block = this.state.blocked==1 ? 0 : 1
      var chatId = this.state.chatId
      var data={
        block:block,
        chatId:chatId,
        contact_id:this.state.other_id,
        command:'block'
      }
      WebSocketInstance.sendMessage(data);
      var arr = this.state.chats;
      var numb_block;
      for(var i=0; i<arr.length;i++){
        if(arr[i].chat_id==chatId){
          var blocked_ = arr[i].blocked!='' ? '' :'true'
          numb_block = arr[i].blocked!='' ? 0 :1
          arr[i].blocked=blocked_;
        }
      }
      this.setState({
        chats:arr,
        blocked:numb_block
      })
      
    }

    render(){
        const messages = this.state.messages;
        //console.log(this.state);
        var block_name = this.state.blocked==1 ? 'Unblock' : 'Block';
        return(
            <div id="frame">
            <Sidepanel 
            username={this.state.currentUser} 
            handleContact={this.renderChat} 
            full_name={this.state.full_name}
            photo = {this.state.profile_url}
            curr_chat = {this.state.chatId} 
            />
    <div className="content">
      <Header 
        other_profile_url= {this.state.other_profile_url}
        other_name = {this.state.other_name}
        other_id = {this.state.other_id}
        blocked = {this.state.blocked}
        renderBlock={this.handleBlock}
        self_blocked={this.state.self_blocked}
      />
      <div className="messages">
        <ul id="chat-log">
          {
              messages &&
              this.renderMessages(messages)
          }
          <div style={{ float:"left", clear: "both" }}
                        ref={(el) => { this.messagesEnd = el; }}>
                    </div>
        </ul>
      </div>
      <div className="message-input">
      <form onSubmit={this.sendMessageHandler}>
        <div className="wrap">
        <input
            onChange={this.messageChangHandler}
            value={this.state.message}
         id="chat-message-input"
          type="text" 
          placeholder="Write your message..." />
        <label htmlFor="file_upload" className="custom-file-upload">
        <i className="fa fa-paperclip attachment" aria-hidden="true"></i>
        </label>
        <input id="file_upload" style={{display:"none"}} onChange={this.file_submit} multiple type="file"/>
        <button id="chat-message-submit" className="submit">
          <i className="fa fa-paper-plane" aria-hidden="true"></i>
        </button>
        </div>
        </form>
      </div>
    </div>
  </div>
        );
    }
}
class App extends React.Component{
  
    // componentDidMount(){
    //   WebSocketInstance.connect();
    // }
  
    render() {
      return (
        // <Router>
        //   <div>
        <Chat />
        // <BaseRouter /> 
        // </div>
        
        // </Router>
        
      );
    }
  }
  
// This optional code is used to register a service worker.
// register() is not called by default.

// This lets the app load faster on subsequent visits in production, and gives
// it offline capabilities. However, it also means that developers (and users)
// will only see deployed updates on subsequent visits to a page, after all the
// existing tabs open on the page have been closed, since previously cached
// resources are updated in the background.

// To learn more about the benefits of this model and instructions on how to
// opt-in, read https://bit.ly/CRA-PWA

// const isLocalhost = Boolean(
//     window.location.hostname === 'localhost' ||
//       // [::1] is the IPv6 localhost address.
//       window.location.hostname === '[::1]' ||
//       // 127.0.0.1/8 is considered localhost for IPv4.
//       window.location.hostname.match(
//         /^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/
//       )
//   );
  
//   function register(config) {
//     if (process.env.NODE_ENV === 'production' && 'serviceWorker' in navigator) {
//       // The URL constructor is available in all browsers that support SW.
//       const publicUrl = new URL(process.env.PUBLIC_URL, window.location.href);
//       if (publicUrl.origin !== window.location.origin) {
//         // Our service worker won't work if PUBLIC_URL is on a different origin
//         // from what our page is served on. This might happen if a CDN is used to
//         // serve assets; see https://github.com/facebook/create-react-app/issues/2374
//         return;
//       }
  
//       window.addEventListener('load', () => {
//         const swUrl = `${process.env.PUBLIC_URL}/service-worker.js`;
  
//         if (isLocalhost) {
//           // This is running on localhost. Let's check if a service worker still exists or not.
//           checkValidServiceWorker(swUrl, config);
  
//           // Add some additional logging to localhost, pointing developers to the
//           // service worker/PWA documentation.
//           navigator.serviceWorker.ready.then(() => {
//             //console.log(
//               'This web app is being served cache-first by a service ' +
//                 'worker. To learn more, visit https://bit.ly/CRA-PWA'
//             );
//           });
//         } else {
//           // Is not localhost. Just register service worker
//           registerValidSW(swUrl, config);
//         }
//       });
//     }
//   }
  
//   function registerValidSW(swUrl, config) {
//     navigator.serviceWorker
//       .register(swUrl)
//       .then(registration => {
//         registration.onupdatefound = () => {
//           const installingWorker = registration.installing;
//           if (installingWorker == null) {
//             return;
//           }
//           installingWorker.onstatechange = () => {
//             if (installingWorker.state === 'installed') {
//               if (navigator.serviceWorker.controller) {
//                 // At this point, the updated precached content has been fetched,
//                 // but the previous service worker will still serve the older
//                 // content until all client tabs are closed.
//                 //console.log(
//                   'New content is available and will be used when all ' +
//                     'tabs for this page are closed. See https://bit.ly/CRA-PWA.'
//                 );
  
//                 // Execute callback
//                 if (config && config.onUpdate) {
//                   config.onUpdate(registration);
//                 }
//               } else {
//                 // At this point, everything has been precached.
//                 // It's the perfect time to display a
//                 // "Content is cached for offline use." message.
//                 //console.log('Content is cached for offline use.');
  
//                 // Execute callback
//                 if (config && config.onSuccess) {
//                   config.onSuccess(registration);
//                 }
//               }
//             }
//           };
//         };
//       })
//       .catch(error => {
//         console.error('Error during service worker registration:', error);
//       });
//   }
  
//   function checkValidServiceWorker(swUrl, config) {
//     // Check if the service worker can be found. If it can't reload the page.
//     fetch(swUrl)
//       .then(response => {
//         // Ensure service worker exists, and that we really are getting a JS file.
//         const contentType = response.headers.get('content-type');
//         if (
//           response.status === 404 ||
//           (contentType != null && contentType.indexOf('javascript') === -1)
//         ) {
//           // No service worker found. Probably a different app. Reload the page.
//           navigator.serviceWorker.ready.then(registration => {
//             registration.unregister().then(() => {
//               window.location.reload();
//             });
//           });
//         } else {
//           // Service worker found. Proceed as normal.
//           registerValidSW(swUrl, config);
//         }
//       })
//       .catch(() => {
//         //console.log(
//           'No internet connection found. App is running in offline mode.'
//         );
//       });
//   }
  
//   function unregister() {
//     if ('serviceWorker' in navigator) {
//       navigator.serviceWorker.ready.then(registration => {
//         registration.unregister();
//       });
//     }
//   }
  


ReactDOM.render(
  
  <App />
  
  
  
  , document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
register();
