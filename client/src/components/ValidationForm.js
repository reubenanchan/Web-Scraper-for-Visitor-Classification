import React, { useState } from "react";
import { Button, Checkbox, Form, FormField, Header } from "semantic-ui-react";
import { resetQNA } from "../redux/reducers/actions";
import { useSelector, useDispatch } from "react-redux";

const ValidationForm = () => {
  const qna = useSelector((state) => state.qna.qna.questions);
  const title = useSelector((state) => state.qna.qna.title);
  const url = useSelector((state) => state.qna.qna.url);
  const [responses, setResponses] = useState({});
  const dispatch = useDispatch();

  const handleChange = (question, value) => {
    setResponses((prevResponses) => ({
      ...prevResponses,
      [question]: value,
    }));
  };

  const handleSubmit = () => {
    dispatch(resetQNA());
    const formattedResponses = Object.entries(responses).map(
      ([question, answer]) => ({
        [`Question`]: { question, answer },
      })
    );
    const outputForm = {
      title: title,
      url: url,
      responses: formattedResponses,
    };

    console.log("Formatted Responses:", outputForm);
    alert("Thank you! Your responses have been submitted.");
    setResponses({});
  };

  const isSubmitDisabled = qna && qna.some((item) => !responses[item.question]);

  return (
    <Form>
      <Header as="h2">{title}</Header>
      {qna && qna.length > 0 ? (
        qna.map((item, index) => (
          <div key={index} style={{ marginBottom: "20px" }}>
            <FormField>
              <Header as="h3">{item.question}</Header>
            </FormField>
            {item.choices.map((choice) => (
              <FormField key={choice}>
                <Checkbox
                  radio
                  label={choice}
                  name={`question-${index}`}
                  value={choice}
                  checked={responses[item.question] === choice}
                  onChange={(e, data) =>
                    handleChange(item.question, data.value)
                  }
                />
              </FormField>
            ))}
          </div>
        ))
      ) : (
        <p></p>
      )}
      {qna && qna.length > 0 && (
        <div>
          {isSubmitDisabled && (
            <p style={{ color: "red" }}>
              Please answer all questions to submit.
            </p>
          )}
          <Button
            type="button"
            color="blue"
            onClick={handleSubmit}
            disabled={isSubmitDisabled}
          >
            Submit
          </Button>
        </div>
      )}
    </Form>
  );
};

export default ValidationForm;
