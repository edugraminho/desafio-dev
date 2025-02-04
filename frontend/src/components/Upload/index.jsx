import React, {Component} from "react";
import Dropzone from "react-dropzone";
import {DropContainer, UploadMessage} from './styles'

export default class Upload extends Component{
  renderDragMessage = (isDragActive, isDragReject) => {
    if (!isDragActive){
      return <UploadMessage> Arraste o arquivo txt aqui...</UploadMessage>
    }
    if (isDragReject){
      return <UploadMessage type="error"> Arquivo nao suportado</UploadMessage>
    }
    return <UploadMessage type="success">Solte os arquivos txt aqui </UploadMessage>
  };

  render(){
    const { onUpload } = this.props

    return (<Dropzone accept='text/*' onDropAccepted={onUpload}> 
      {({getRootProps, getInputProps, isDragActive, isDragReject}) => 
      
      < DropContainer
          {... getRootProps()}
          isDragActive={isDragActive}
          isDragReject={isDragReject}
      > 
        <input {...getInputProps()}/>
        {this.renderDragMessage(isDragActive, isDragReject)}
      </DropContainer>}
    </Dropzone>)
  }
}