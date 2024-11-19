export const increment = () => ({
  type: "INCREMENT",
});

export const decrement = () => ({
  type: "DECREMENT",
});

export const SET_QNA = "SET_QNA";

export const setQNA = (qna) => ({
  type: SET_QNA,
  payload: qna,
});
