---
title: Dividir PDF usando JavaScript
linktitle: Dividir arquivos PDF
type: docs
weight: 30
url: /javascript-cpp/split-pdf/
description: Este tópico mostra como dividir páginas de PDF em arquivos PDF individuais com Aspose.PDF para JavaScript via C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Dividir PDF em dois arquivos usando JavaScript

Este tópico mostra como dividir páginas de PDF em arquivos PDF individuais usando JavaScript. Atualmente, suportamos a divisão em duas partes. Isso significa que `pageToSplit` é um marcador para divisão. O primeiro arquivo conterá todas as páginas de 1 a `pageToSplit` inclusive, e o segundo arquivo terá o restante das páginas.

A operação de divisão depende do número de páginas no documento e pode ser muito demorada. Portanto, recomendamos fortemente o uso de Web Workers.

O trecho de código fornecido é um exemplo de uso de um Web Worker em JavaScript para dividir um arquivo PDF em dois arquivos PDF separados e oferecer ao usuário a opção de baixar os arquivos resultantes.
 Aqui estão os passos do código:

1. Criando um Web Worker. Um web worker é inicializado usando o arquivo de script "AsposePDFforJS.js". Este web worker irá lidar com as tarefas de divisão de arquivos PDF em segundo plano. Em nosso exemplo, quaisquer erros que ocorram no worker são capturados e registrados no console.
2. Manipulação de Mensagens. O web worker é configurado para escutar mensagens usando o manipulador de eventos onmessage. Quando ele recebe uma mensagem da página web, ele processa a solicitação e envia uma resposta de volta para o thread principal.
3. Manipulador de Evento de Divisão de Arquivo. Existe um manipulador de evento ffileSplit que é acionado quando um usuário seleciona um arquivo PDF para dividir. Ele lê o arquivo PDF selecionado usando um FileReader e envia o conteúdo do arquivo e os parâmetros relevantes (como o número de páginas a dividir e os nomes dos arquivos de saída) para o web worker via uma chamada postMessage.
1. Função de Download de Arquivo. A função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) é responsável por gerar um link que permite ao usuário baixar um arquivo. Ela aceita o nome do arquivo, tipo MIME e conteúdo do arquivo. A função cria um link de download, associa o conteúdo do arquivo a ele, define o nome do arquivo e o adiciona ao documento. Isso permite que o usuário baixe os arquivos PDF resultantes.

1. Manipulação de Mensagens no Web Worker. Em seguida, se o 'json.errorCode' for 0, então json.fileNameResult conterá o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre tal erro estarão contidas na propriedade 'json.errorText'.

1. Exibição de Resultado. A página principal inclui um elemento com o ID 'output'. Quando o web worker envia uma mensagem com o resultado, ele atualiza o elemento 'output'. Se a operação for bem-sucedida, ele exibe links para download dos dois arquivos PDF divididos. Se houver um erro, ele exibe uma mensagem de erro.

Este código demonstra uma maneira de delegar tarefas intensivas em recursos de divisão de arquivos PDF para um web worker para evitar bloquear o thread principal da interface do usuário. Ele também oferece uma maneira amigável para o usuário baixar os arquivos PDF divididos.

```js

    /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ?
          `Resultado:\n${DownloadFile(evt.data.json.fileNameResult1, "application/pdf", evt.data.params[0])}
                  \n${DownloadFile(evt.data.json.fileNameResult2, "application/pdf", evt.data.params[1])}` :
          `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de evento*/
    const ffileSplit = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Definir número de página para dividir*/
        const pageToSplit = 1;
        /*Dividir em dois arquivos PDF e salvar como "ResultSplit1.pdf", "ResultSplit2.pdf" - Perguntar ao Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSplit2Files',
            "params": [event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Criar um link para baixar o arquivo de resultado*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Clique aqui para baixar o arquivo " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```

O seguinte trecho de código JavaScript mostra um exemplo simples de como dividir páginas de um PDF em arquivos PDF individuais:

1. Selecione um arquivo PDF para dividir.
1. Crie um objeto 'FileReader' no manipulador.
1. Defina o número de uma página para dividir.
1. Chame [AsposePdfSplit2Files](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsplit2files/) no último manipulador.
1. Analise o resultado. O nome do arquivo resultante é definido, neste exemplo, como "ResultSplit2.pdf".
1. Em seguida, se o 'json.errorCode' for 0, então json.fileNameResult conterá o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então informações sobre tal erro estarão contidas na propriedade 'json.errorText'.
1. Você pode usar a função auxiliar [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/).

```js

  var ffileSplit = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Defina o número de uma página para dividir*/
      const pageToSplit = 1;
      /*Divida em dois arquivos PDF e salve como "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfSplit2Files(event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = e.target.files[0].name + " dividido: " + json.fileNameResult1 + ", " + json.fileNameResult2;
      else document.getElementById('output').textContent = json.errorText;
      /*Crie um link para baixar o primeiro arquivo de resultado*/
      DownloadFile(json.fileNameResult1, "application/pdf");
      /*Crie um link para baixar o segundo arquivo de resultado*/
      DownloadFile(json.fileNameResult2, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```