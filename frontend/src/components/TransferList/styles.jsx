import styled from "styled-components";
import { Card } from "antd";


export const Container = styled.div`
  display: flex;
  padding: 1vw;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

export const StyledCard = styled(Card)`
  margin: 10px;
  width: 160px;
  border: 1.5px dashed #ddd;
  border-radius: 4px;
`;

export const StyledList = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
`;

export const Button = styled.button`
  padding: 8px;
  font-size: 10px;
  border-radius: 4px;
`;

export const Text = styled.div`
    font-size: 10px;
    margin: 4px;
`;

