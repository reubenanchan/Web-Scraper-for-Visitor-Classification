import { SET_QNA } from "./actions";

const initialState = {
  qna: [],
};

const qnaReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_QNA:
      return {
        ...state,
        qna: action.payload,
      };
    default:
      return state;
  }
};

export default qnaReducer;
