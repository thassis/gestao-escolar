import React from "react";
import { BrowserRouter, Routes, Route, Router } from "react-router-dom";
import Login from "./pages/login/Login";
import Home from "./pages/home/Home";
import NoPage from "./pages/no-page/NoPage";
import { ThemeProvider as MuiThemeProvider } from "@mui/material";
import { ThemeProvider } from "@emotion/react";
import { createTheme } from "@mui/material/styles";
import Footer from "./shared-components/footer/Footer";
import RegisterStudent from "pages/register-student/RegisterStudent";

let theme = createTheme({
  palette: {
    primary: {
      main: "#A5CEF4",
    },
    secondary: {
      main: "#E19626",
    },
    text: {
      primary: "#000",
    },
  },
});

function App() {
  return (
    <MuiThemeProvider theme={theme}>
      <ThemeProvider theme={theme}>
        <BrowserRouter>
          <Routes>
            <Route path="/">
              <Route index element={<Login />} />
              <Route path="home" element={<Home />} />
              <Route path="register-student" element={<RegisterStudent />} />
              <Route path="*" element={<NoPage />} />
            </Route>
          </Routes>
        </BrowserRouter>
        <Footer />
      </ThemeProvider>
    </MuiThemeProvider>
  );
}

export default App;
