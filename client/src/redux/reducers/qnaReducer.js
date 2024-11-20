import { SET_QNA, RESET_QNA } from "./actions";

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
    case RESET_QNA:
      return initialState;
    default:
      return state;
  }
};

export default qnaReducer;
