import { combineReducers } from "redux";
import counterReducer from "./counterReducer";
import qnaReducer from "./qnaReducer";
import isLoadingReducer from "./isLoadingReducer";

export default combineReducers({
  counter: counterReducer,
  qna: qnaReducer,
  isLoading: isLoadingReducer,
});
