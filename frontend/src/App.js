import { useState } from "react";
import axios from "axios";
import HighlightedText from "./components/corrected_text";
import 'bootstrap/dist/css/bootstrap.min.css';
import DropDown from "./components/dropdown";


const colorTheme = {
  background: "#ffffff",
  msgUser: "#CCCCFF",
  msgTandem: "#BEECCF",
  msgCorrection: "#E5EFFA",
  msgBackground: "#E5EFFA",
  button: "",
  inputBackground: "#E5EFFA"
}

const roleColors = {
  user: colorTheme.msgUser,
  tandem: colorTheme.msgTandem,
  correction: colorTheme.msgCorrection
};

const roleAllign = {
  user: "right",
  tandem: "left",
  correction: "right",
};

const rolePrefix = {
  user: "Toi:",
  tandem: "Tandem:",
  correction: "Correction:",
}


function App() {
  const [input, setInput] = useState("");
  const [chat, setChat] = useState([]); // chat history
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    const trimmed = input.trim();
    if (!trimmed) return;
  
    // Optimistic update (optional)
    const newChat = [...chat, { role: "user", content: trimmed }];
    setChat(newChat);
    setInput("");
    setLoading(true);
  
    try {
      const res = await axios.post("http://localhost:8000/api/chat/", {
        message: trimmed,
      });
  
      // Replace with full chat history from backend
      const fullHistory = res.data.history.map((msg) => ({
        role: msg.role,
        content: msg.content,
      }));
  
      setChat(fullHistory);
    } catch (err) {
      setChat([
        ...newChat,
        { role: "assistant", content: "❌ Erreur lors de l'envoi du message. "  + err},
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleLoadAll = async () => {
    try {
      const res = await axios.get("http://localhost:8000/api/load_sessions/");

      // Replace with full chat history from backend
      const fullHistory = res.data.history.map((msg) => ({
        role: msg.role,
        content: msg.content,
      }));
  
      setChat(fullHistory);
    } catch (err) {
      setChat([
        { role: "assistant", content: "❌ Error Loading Messages. "  + err},
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleLoadPreviousSession = async () => {
    try {
      const res = await axios.get("http://localhost:8000/api/load_previous_sessions/");

      // Replace with full chat history from backend
      const fullHistory = res.data.history.map((msg) => ({
        role: msg.role,
        content: msg.content,
      }));
  
      setChat(fullHistory);
    } catch (err) {
      setChat([
        { role: "assistant", content: "❌ Error Loading Messages. "  + err},
      ]);
    } finally {
      setLoading(false);
    }
  };


  return (
    <div style={{ 
      padding: "2rem", 
      fontFamily: "sans-serif", 
      background:colorTheme.background, 
      position: "absolute",
      top: "0px",
      bottom: "0px", 
      width: "100%",
      }}>

    <div className="container mt-4">
          <div className="row" style={{marginBottom:"2rem"}}>
            <div className="col-8">
              <h2>🇫🇷 French Tandem Chat</h2>
              </div>
            <div className="col d-flex justify-content-end" >
                <div style={{width:"20%", height:"50%", align:"right"}}>
                  <DropDown
                    handleLoadPreviousSession={handleLoadPreviousSession}
                    handleLoadAll={handleLoadAll}
                  />
                </div>
            </div>
          </div>

      </div>




      <div
        style={{
          border: "1px solid #ccc",
          borderRadius: "0.5rem",
          padding: "1rem",
          marginBottom: "1rem",
          maxHeight: "400px",
          overflowY: "auto",
          width:"100%",
          height:"100%",
          backgroundColor: colorTheme.msgBackground,
        }}
      >
        {chat.map((msg, idx) => (
          <div
            key={idx}
            style={{
              marginBottom: "1rem",
              textAlign: roleAllign[msg.role],
            }}
          >
            <div
              style={{
                display: "inline-block",
                backgroundColor: roleColors[msg.role], 
                padding: "0.5rem 1rem",
                borderRadius: "12px",
                maxWidth: "80%",
              }}
            >
              <strong>{rolePrefix[msg.role]}</strong>{" "}
              <HighlightedText text={msg.content}/>
            </div>
          </div>
        ))}
      </div>
      <textarea
        style={{ width: '100%', padding: '1rem', borderRadius: '0.5rem', border: '1px solid #ccc', background:colorTheme.inputBackground }}
        rows="4"
        cols="60"
        placeholder="Écris ton message ici..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        disabled={loading}
      />

      <br />
      <button  style={{width:"100%", align:"center", marginTop:"1rem"}} onClick={handleSend} disabled={loading}>
        {loading ? "Envoi..." : "Envoyer"}
      </button>

      <br />
        
    </div>
  );
}

export default App;