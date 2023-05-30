import React, { useState, useEffect } from "react";
import { useParams, Link, useLocation, useNavigate } from "react-router-dom";
import { Typography, TextField, Button, Grid } from "@mui/material";
import {
  IPeriodoLetivo,
  PeriodoLetivoServices,
} from "services/periodo-letivo/PeriodoLetivoServices";
import Header from "shared-components/header/Header";
import { BoxList } from "./styles";

const EditPeriodoLetivo = () => {
  const navigate = useNavigate();
  const location = useLocation();

  const periodoLetivoParams = location.state as IPeriodoLetivo;

  const [periodoLetivo, setPeriodoLetivo] = useState<IPeriodoLetivo>({
    ...periodoLetivoParams,
    start_date: new Date(periodoLetivoParams.start_date).toLocaleDateString(),
    end_date: new Date(periodoLetivoParams.end_date).toLocaleDateString(),
  });

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setPeriodoLetivo((prevPeriodoLetivo) => ({
      ...prevPeriodoLetivo,
      [name]: value,
    }));
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    PeriodoLetivoServices.update(periodoLetivo)
      .then((response) => {
        alert("Período letivo atualizado com sucesso!");
        navigate("/periodo-letivo");
      })
      .catch((error) => {
        alert("Ocorreu um erro ao atualizar o período letivo!");
      });
  };

  return (
    <div>
      <Header />
      <BoxList marginTop={"16px"}>
        <Typography variant="h6" gutterBottom>
          Editar Período Letivo
        </Typography>
        <form onSubmit={handleSubmit}>
          <Grid container spacing={2}>
            <Grid item xs={12}>
              <TextField
                name="id"
                label="ID"
                value={periodoLetivo.id}
                disabled
                fullWidth
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                name="start_date"
                label="Data de Início"
                value={periodoLetivo.start_date}
                onChange={handleInputChange}
                fullWidth
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                name="end_date"
                label="Data de Término"
                value={periodoLetivo.end_date}
                onChange={handleInputChange}
                fullWidth
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                name="class_shift"
                label="Turno"
                value={periodoLetivo.class_shift}
                onChange={handleInputChange}
                fullWidth
              />
            </Grid>
            <Grid item xs={12}>
              <Button type="submit" variant="contained" color="primary">
                Salvar
              </Button>
              <Button
                component={Link}
                to="/periodo-letivo"
                variant="contained"
                color="secondary"
                style={{ marginLeft: 10 }}
              >
                Cancelar
              </Button>
            </Grid>
          </Grid>
        </form>
      </BoxList>
    </div>
  );
};

export default EditPeriodoLetivo;
