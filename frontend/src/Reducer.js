// frontend/src/Reducer.js
import { combineReducers } from "redux";
import { connectRouter } from "connected-react-router";

// import new reducer
import { signupReducer } from "./components/signup/SignupReducer";
import { loginReducer } from "./components/login/LoginReducer"; // add import
import { notesReducer } from "./components/notes/NotesReducer";

const createRootReducer = history =>
  combineReducers({
    router: connectRouter(history),
    createUser: signupReducer, // <--- add it here
    auth: loginReducer, // <--- add reducer
    notes: notesReducer // added notesReducer
  });

export default createRootReducer;
