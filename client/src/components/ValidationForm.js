import React, { useState } from "react";
import { Button, Checkbox, Form, FormField, Header } from "semantic-ui-react";

const ValidationForm = ({ qna }) => {
  const [responses, setResponses] = useState({});

  const handleChange = (question, value) => {
    setResponses((prevResponses) => ({
      ...prevResponses,
      [question]: value,
    }));
  };

  const handleSubmit = () => {
    const formattedResponses = Object.entries(responses).map(
      ([question, answer]) => ({
        [`Question`]: { question, answer },
      })
    );

    console.log("Formatted Responses:", formattedResponses);
    alert("Thank you! Your responses have been submitted.");
  };

  return (
    <Form>
      {qna.map((item, index) => (
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
                onChange={(e, data) => handleChange(item.question, data.value)}
              />
            </FormField>
          ))}
        </div>
      ))}
      <Button type="button" color="blue" onClick={handleSubmit}>
        Submit
      </Button>
    </Form>
  );
};

export default ValidationForm;
