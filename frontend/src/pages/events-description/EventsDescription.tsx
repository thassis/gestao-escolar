import React from "react";
import { Box } from '@mui/system';
import { useLocation, useNavigate } from "react-router-dom";
import { Button, Card, CardActionArea, CardContent, Grid, IconButton, Paper, Typography } from "@mui/material";
import CardMedia from '@mui/material/CardMedia';

import Header from "shared-components/header/Header";
import { Descricao, Subtitle } from "./styles";
import { nextEvent } from "data-front/nextEvent";
import { MenuList } from "data-front/data";

import { EventParams } from "pages/scheduled-events/ScheduledEvents";

const EventsDescription = () => {

  const location = useLocation();
  const { name, id, date, description } = location.state;

  const onNavigateAddPhotos = () =>{
    window.location.replace('/events-add-photos');
  }

  
  return (
    <>
      <Header />
      
      <Box margin={4}>
        <Box ml={7}>
          <Subtitle variant="h4" gutterBottom>
            {name}
          </Subtitle>
          <Typography variant="h5">
            Descrição do evento
          </Typography>

          <Typography variant="body1">
            {date.toLocaleDateString()}
          </Typography>

          <Typography variant="body1">
            {description}
          </Typography>

        </Box>

      </Box>
    </>
  );
};

export default EventsDescription;
