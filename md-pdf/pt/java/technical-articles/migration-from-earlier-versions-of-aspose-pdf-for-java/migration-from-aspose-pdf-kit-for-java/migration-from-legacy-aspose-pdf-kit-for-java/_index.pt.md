---
title: Migração do Aspose.Pdf.Kit legado para Java
type: docs
weight: 10
url: /java/migration-from-legacy-aspose-pdf-kit-for-java/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

O componente atual Aspose.PDF.Kit para Java oferece recursos para manipular arquivos PDF existentes. No entanto, em breve, este componente será descontinuado como produto separado, pois transferimos todas as suas classes e enumerações para o pacote **com.aspose.pdf.facades** da nova versão autoportada do Aspose.PDF para Java (4.x.x). Agora esta única versão autoportada oferece capacidades para criar e manipular arquivos PDF existentes.

{{% /alert %}}

## Suporte para código legado

Durante toda a atividade de migração, definitivamente consideramos o impacto dessa atividade sobre os clientes existentes e tentamos ao máximo minimizar esse impacto tanto quanto possível.
 Além disso, também nos concentramos em tornar o novo lançamento autoportado compatível com versões anteriores, para que a base de código dos clientes existentes exija mudanças mínimas. Mesmo que o novo lançamento autoportado forneça o Document Object Model (DOM) no pacote com.aspose.pdf para criar e manipular arquivos PDF existentes, ainda assim, se você quiser continuar usando seu código legado desenvolvido com Aspose.PDF.Kit para Java, você só precisa importar o pacote **com.aspose.pdf.facades** e seu código deve funcionar (*exceto para atualização de referências de classes explícitas*).

O snippet de código a seguir mostra como executar seu código Aspose.PDF.Kit para Java existente com o novo Aspose.PDF para Java autoportado.

```java

 import com.aspose.pdf.facades.*;

public class template {

    public static void main(String[] args) {

        try{

            // carregar arquivo PDF existente

            com.aspose.pdf.facades.PdfFileInfo fileInfo = new com.aspose.pdf.facades.PdfFileInfo("input.pdf");

            System.out.println("TÍTULO: " + fileInfo.getTitle());

            System.out.println("AUTOR:" + fileInfo.getAuthor());

            System.out.println("DATADECRIAÇÃO:" + fileInfo.getCreationDate());

            System.out.println("CRIADOR:" + fileInfo.getCreator());

            System.out.println("PALAVRAS-CHAVE:" + fileInfo.getKeywords());

            System.out.println("DATAMODIFICAÇÃO:" + fileInfo.getModDate());

           }


catch(Exception ex)


{System.out.println(ex);}


}

}
```

## Usando a classe ReplaceTextStrategy

Para migrar o código para a classe ReplaceTextStrategy, o método **setScope(..)** foi atualizado para **setReplaceScope(..)**. Por favor, veja o trecho de código a seguir.

```java

 // instanciar objeto PdfContentEditor

com.aspose.pdf.facades.PdfContentEditor editor = new com.aspose.pdf.facades.PdfContentEditor();

// vincular arquivo PDF de origem

editor.bindPdf("input.pdf");

// criar estratégia de substituição de texto

com.aspose.pdf.facades.ReplaceTextStrategy strategy = new com.aspose.pdf.facades.ReplaceTextStrategy();

// definir o alinhamento para substituição de texto

strategy.setAlignment(com.aspose.pdf.facades.AlignmentType.Left);

// escopo para substituição de texto

strategy.setReplaceScope(com.aspose.pdf.facades.ReplaceTextStrategy.Scope.REPLACE_ALL);

// definir a estratégia de substituição

editor.setReplaceTextStrategy(strategy);

editor.replaceText("test","replaced");

// salvar arquivo atualizado

editor.save("TxtReplaceTest.pdf");
```