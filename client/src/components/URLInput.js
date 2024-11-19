import React, { useState } from "react";
import axios from "axios";
import { Form, Input } from "semantic-ui-react";
import { setQNA } from "../redux/reducers/actions";
import { useDispatch, useSelector } from "react-redux";

const URLInput = () => {
  const [url, setURL] = useState("");
  const qna = useSelector((state) => state.qna.qna);
  const dispatch = useDispatch();

  const handleSubmit = async () => {
    console.log(url);
    axios
      .post("/submit_url", {
        url: url,
      })
      .then(function (response) {
        console.log(response);
        console.log(response.data);
        dispatch(setQNA(response.data));
      })
      .catch(function (error) {
        console.error("Error:", error);
      });
  };

  return (
    <Form>
      <Form.Field>
        <div class="ui action input">
          <input
            type="text"
            placeholder="Enter a URL"
            value={url}
            onChange={(e) => setURL(e.target.value)}
          />
          <button class="ui button" onClick={handleSubmit}>
            Search
          </button>
        </div>
      </Form.Field>
    </Form>
  );
};

export default URLInput;
