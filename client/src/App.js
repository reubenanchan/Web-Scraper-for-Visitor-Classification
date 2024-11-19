import React, { useEffect, useState } from "react";
import Counter from "./components/counter";
import URLInput from "./components/URLInput";
import ValidationForm from "./components/ValidationForm";
import { Container, Header } from "semantic-ui-react";
import { setQNA } from "./redux/reducers/actions";
import { useDispatch, useSelector } from "react-redux";

const App = () => {
  const dispatch = useDispatch();
  const qna = useSelector((state) => state.qna.qna);

  /*
  useEffect(() => {
    fetch("/test").then((response) =>
      response.json().then((data) => {
        setQNA(data);
      })
    );
  }, []);
  */
  //console.log(qna);

  return (
    <div className="">
      <Container style={{ marginTop: 40 }}>
        <Header as="h1" textAlign="center">
          Web Scraper for Visitor Classification
        </Header>
      </Container>
      <Container style={{ marginTop: 40 }}>
        <URLInput />
      </Container>
      <Container style={{ marginTop: 40 }}>
        <ValidationForm qna={qna} />
      </Container>
    </div>
  );
};

export default App;
