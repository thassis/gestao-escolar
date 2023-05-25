import { Box, Paper } from '@mui/material'
import { styled } from '@mui/material/styles';

export const PaperList = styled(Paper)(({theme}) => ({
  padding: '2px 4px',
  display: 'flex',
  alignItems: 'center',
  width: 600,
  margin: '20px',
}))

export const BoxList = styled(Box)(({theme}) => ({
  display: 'flex',
  flexDirection: 'column',
  textAlign: 'center',
}))