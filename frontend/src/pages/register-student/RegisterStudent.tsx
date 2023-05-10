import React, { useState } from "react";
import Header from "../../shared-components/header/Header";
import { Body, LoginButton } from "./styles";
import { TextField } from "@mui/material";
import { useNavigate } from "react-router-dom";

const RegisterStudent = () => {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [errorEmail, setErrorEmail] = useState(false);

  const [password, setPassword] = useState("");
  const [errorPassword, setErrorPassword] = useState(false);

  const updateErrorInputs = () => {
    if (!email) {
      setErrorEmail(true);
    } else {
      setErrorEmail(false);
    }

    if (!password) {
      setErrorPassword(true);
    } else {
      setErrorPassword(false);
    }
  };

  const onClickEnter = () => {
    updateErrorInputs();

    if (email && password) {
      navigate("home");
    }
  };

  return (
    <>
      <Header />
      <Body>
        <TextField
          type="email"
          error={errorEmail}
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          label="E-mail"
          variant="outlined"
        />

        <TextField
          error={errorPassword}
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          label="Senha"
          variant="outlined"
        />

        <LoginButton variant="contained" onClick={() => onClickEnter()}>
          Entrar
        </LoginButton>
      </Body>
    </>
  );
};

export default RegisterStudent;
