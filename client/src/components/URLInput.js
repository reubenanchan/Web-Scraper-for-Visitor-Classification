import React, { useState } from "react";
import axios from "axios";
import { Form, Input } from "semantic-ui-react";

const URLInput = () => {
  const [url, setURL] = useState("");
  const [qna, setQNA] = useState([]);

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
          <button
            class="ui button"
            onClick={async () => {
              console.log(url);
              axios
                .post("/submit_url", setQNA)
                .then(function (response) {
                  console.log(response);
                  console.log(response.data);
                  setQNA(response.data);
                })
                .catch(function (error) {
                  console.error("Error:", error);
                });
            }}
          >
            Search
          </button>
        </div>
      </Form.Field>
      <pre>{JSON.stringify(qna, null, 2)}</pre>
    </Form>
  );
};

export default URLInput;
