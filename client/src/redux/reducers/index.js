import { combineReducers } from "redux";
import counterReducer from "./counterReducer";
import qnaReducer from "./qnaReducer";

export default combineReducers({
  counter: counterReducer,
  qna: qnaReducer,
});
