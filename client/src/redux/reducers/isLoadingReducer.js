import { START_LOADING, STOP_LOADING } from "./actions";

const initialState = false;

const isLoadingReducer = (state = initialState, action) => {
  switch (action.type) {
    case START_LOADING:
      return true;
    case STOP_LOADING:
      return false;
    default:
      return state;
  }
};

export default isLoadingReducer;
