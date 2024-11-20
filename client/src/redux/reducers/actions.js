export const increment = () => ({
  type: "INCREMENT",
});

export const decrement = () => ({
  type: "DECREMENT",
});

export const SET_QNA = "SET_QNA";

export const RESET_QNA = "RESET_QNA";

export const setQNA = (qna) => ({
  type: SET_QNA,
  payload: qna,
});

export const resetQNA = () => ({
  type: RESET_QNA,
});

export const START_LOADING = "START_LOADING";

export const STOP_LOADING = "STOP_LOADING";

export const startLoading = () => ({
  type: START_LOADING,
});

export const stopLoading = () => ({
  type: STOP_LOADING,
});
