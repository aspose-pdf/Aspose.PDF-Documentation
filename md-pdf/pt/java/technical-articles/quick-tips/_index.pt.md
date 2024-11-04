---
title: Dicas Rápidas
type: docs
weight: 50
url: /java/quick-tips/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página contém algumas dicas rápidas relacionadas à API Aspose.PDF para Java

{{% /alert %}}

## Adicionar JavaScript ao PDF

O seguinte trecho de código pode ser usado para definir/adicionar JavaScript ao arquivo PDF.

```java

String path = "D:\\";
String fileOut = path + "JavaScript.pdf";
IDocument document = null;
try
{

    document = new Document();
    document.getPages().add();
    document.getPages().add();

    //Adicionando JavaScript no Nível do Documento
    //Instanciar JavascriptAction com a instrução JavaScript desejada
    JavascriptAction javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

    //Atribuir o objeto JavascriptAction à ação desejada do Documento
    document.setOpenAction(javaScript);
    document.setOpenAction(new JavascriptAction("app.alert('Hello PDF')"));

    //Adicionando JavaScript no Nível da Página
    document.getActions().setBeforeClosing(new JavascriptAction("app.alert('document is closing')"));

    document.getPages().get_Item(1).getActions().setOnOpen(new JavascriptAction("app.alert('page 1 is opened')"));

    document.getPages().get_Item(2).getActions().setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));

    document.getPages().get_Item(2).getActions().setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

    document.save(fileOut);

}
finally { if (document != null) document.dispose(); document = null; }

```


**Alguns mais exemplos**

```java

// após a impressão
document.getActions().setAfterPrinting(new JavascriptAction("app.alert('Arquivo foi impresso')"));

// após salvar
document.getActions().setAfterSaving(new JavascriptAction("app.alert('Arquivo foi salvo')"));


```

## Liberar Memória Utilizada

Se você completou o trabalho com Aspose.PDF para Java e deseja limpar a memória de diferentes instâncias estáticas,
para maximizar a memória para outros processos, você deve executar a seguinte linha de código:

```java

 com.aspose.pdf.MemoryCleaner.clear();

```

## Carregar PDF a partir de ByteArrayInputStream

O seguinte trecho de código mostra os passos para carregar o arquivo PDF em ByteArray e então instanciar o objeto Document com ByteArrayInputStream.

```java

 // arquivo PDF fonte

java.io.File file = new java.io.File("c:/pdftest/result.pdf");

java.io.FileInputStream fis = new java.io.FileInputStream(file);

//System.out.println(file.exists() + "!!");

//InputStream in = resource.openStream();

java.io.ByteArrayOutputStream bos = new java.io.ByteArrayOutputStream();

byte[] buf = new byte[1024];

try {

    for (int readNum; (readNum = fis.read(buf)) != -1;) {

        bos.write(buf, 0, readNum); //sem dúvida aqui é 0

        //Escreve len bytes do array de bytes especificado começando no deslocamento off para este fluxo de saída de array de bytes.

        System.out.println("lidos " + readNum + " bytes,");

    }

} catch (java.io.IOException ex) {


}

byte[] bytes = bos.toByteArray();

// instanciar Objeto Document com ByteArrayInputStream enquanto passa o array de bytes como argumento

com.aspose.pdf.Document doc = new 
com.aspose.pdf.Document(new java.io.ByteArrayInputStream(bytes));

// obter a contagem de páginas do arquivo PDF

 System.out.println(doc.getPages().size());

```


## Salvar PDF em ByteArrayOutputStream

O trecho de código a seguir mostra as etapas para salvar o arquivo PDF resultante em um ByteArrayOutputStream.

```java

 com.aspose.pdf.Document pdfDocument = new 
com.aspose.pdf.Document("source.pdf");

java.io.InputStream is = null;

java.io.ByteArrayOutputStream os = new java.io.ByteArrayOutputStream();

try{

pdfDocument.save(os,com.aspose.pdf.SaveFormat.Doc);

System.out.println(os.size());

is = new java.io.ByteArrayInputStream(os.toByteArray());

            os.close();

            os.flush();

pdfDocument.close();

}catch (Throwable e) {}

```