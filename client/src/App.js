import React from "react";
import URLInput from "./components/URLInput";
import ValidationForm from "./components/ValidationForm";
import { Container, Header, Loader } from "semantic-ui-react";
import { useSelector } from "react-redux";

const App = () => {
  const isLoading = useSelector((state) => state.isLoading);

  return (
    <div className="">
      <Container style={{ marginTop: 40 }}>
        <Header as="h1" textAlign="center">
          Web Scraper for Visitor Classification
        </Header>
        <p style={{ textAlign: "center" }}>
          Provide a URL to automatically create tailored questions and
          multiple-choice options to categorize site visitors.
        </p>
      </Container>
      <Container style={{ marginTop: 40 }}>
        <URLInput />
      </Container>
      <Container style={{ marginTop: 40 }}>
        {isLoading ? (
          <Loader active inline="centered" />
        ) : (
          <>
            <ValidationForm />
          </>
        )}
      </Container>
    </div>
  );
};

export default App;
