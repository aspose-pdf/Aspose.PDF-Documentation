---
title: Migrando seu código para Aspose.PDF para Java 2.5.0
type: docs
weight: 10
url: /pt/java/migrating-your-code-to-aspose-pdf-for-java-2-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Neste artigo, tentamos destacar algumas das áreas de um código existente do Aspose.PDF para Java para torná-lo compatível com a versão mais recente.

{{% /alert %}}

## Detalhes

Com o lançamento do Aspose.PDF para Java 2.5.0, houve muitas mudanças na estrutura da API e construção das classes. A maioria dos nomes dos membros da classe foram atualizados, alguns membros de classe existentes foram removidos e também alguns métodos e propriedades foram adicionados às classes existentes. Apenas para dar uma breve noção das alterações, vamos dar uma olhada no seguinte código simples, baseado nas versões do Aspose.PDF para Java publicadas anteriormente à 2.5.0.

Neste código simples, adicionaremos um hyperlink e um link para a página dentro do mesmo documento PDF.

```java
import com.aspose.pdf.elements.*;
com.aspose.pdf.License lic = new com.aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}


//Instanciar um objeto Pdf chamando seu construtor vazio

Pdf pdf1 = new Pdf();

//Criar uma seção no objeto Pdf

Section sec1 = pdf1.getSections().add();

//Criar um parágrafo de texto com a referência de uma seção

Text text1 = new Text(sec1);

//Adicionar o parágrafo de texto na coleção de parágrafos da seção

sec1.getParagraphs().add(text1);

//Adicionar um segmento de texto no parágrafo de texto

Segment segment1 = text1.getSegments().add("este é um link local");

//Definir o texto no segmento de texto para ser sublinhado

segment1.getTextInfo().setUnderLine(true);


//Definir o tipo de link do segmento de texto como Local

//Atribuir o id do parágrafo desejado como um id alvo para o segmento de texto

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

//Criar um parágrafo de texto para ser vinculado ao segmento de texto

Text text3 = new Text(sec1,"informações do produto 1 ...");

//Adicionar o parágrafo de texto à coleção de parágrafos da seção

sec1.getParagraphs().add(text3);

//Definir este parágrafo para ser o primeiro para que possa ser exibido em uma página separada no documento

text3.setFirstParagraph(true);

//Definir o id deste segmento de texto como "product1"

text3.setID("product1"); 


// salvar o arquivo PDF

FileOutputStream out = new FileOutputStream(new File("UpdateOfCode_Test.pdf"));

pdf1.save(out);
```


Quando estiver usando as versões anteriores ao Aspose.PDF para Java 2.5.0, o código pode ser executado com sucesso e um documento PDF resultante contendo um hyperlink para uma página dentro do mesmo documento pode ser gerado. Mas, quando o mesmo código é compilado com a versão 2.5.0, você notará vários erros porque houve mudanças nos membros da classe e também alguns dos métodos nas classes foram removidos. Agora vamos começar com a modificação do código para a versão 2.5.0

Use `import aspose.pdf.*`; em vez de `import com.aspose.pdf.elements.*`; para incluir o pacote.

Para inicialização da licença, por favor atualize seu código existente de

{{% alert color="primary" %}}
**com.aspose.pdf.License lic = new com.aspose.pdf.License();**

```java

try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```

{{% /alert %}}

para

{{% alert color="primary" %}}
**aspose.pdf.License lic = new aspose.pdf.License();**

```java

try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```


{{% /alert %}}

**TextInfo** não contém mais o método **setUnderLine(...)**. Por favor, tente usar **TextInfo.setIsUnderline(...)** **em vez disso**.**

A classe chamada **HyperLinkToLocalPdf** foi removida. Portanto, atualize qualquer código existente como

{{% alert color="primary" %}}
**//Defina o tipo de link do segmento de texto para Local**

```java

 //Atribua o id do parágrafo desejado como um id de destino para o segmento de texto

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

```

{{% /alert %}}

para

{{% alert color="primary" %}}
**segment1.getHyperlink().setLinkType(HyperlinkType.Local);**

```java

 segment1.getHyperlink().setTargetID("product1");

```

{{% /alert %}}

O nome do método **setFirstParagraph** foi removido da classe Text.
 Para exibir o segmento de texto em uma nova página, você precisa criar um novo objeto Section e adicionar o objeto de texto à seção recém-criada. Como por padrão, cada seção é exibida em uma nova página, não há necessidade de chamar um método como **sec2.setIsNewPage(true**)**;

## Método de Salvamento Atualizado

O método save na classe Pdf, que costumava ter um objeto FileOutputStream como argumento, foi removido. Na nova versão, você pode usar qualquer um dos seguintes métodos sobrecarregados de save.

- save(BasicStream stream)
- save(java.lang.String pdfFile)
- save(java.lang.String fileName, SaveType saveType, aspose.pdf.HttpResponse response)

Depois de fazer todas as alterações especificadas acima, ao usar o Aspose.PDF para Java 2.5.0, o código será compilado e executado sem mostrar nenhuma mensagem de erro. O trecho de código atualizado completo é especificado abaixo.

```java
import aspose.pdf.*;
aspose.pdf.License lic = new aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}

try {

//Instanciar um objeto Pdf chamando seu construtor vazio

Pdf pdf1 = new Pdf();

//Criar uma seção no objeto Pdf

Section sec1 = pdf1.getSections().add();

//Criar parágrafo de texto com a referência de uma seção

Text text1 = new Text(sec1);

//Adicionar o parágrafo de texto à coleção de parágrafos da seção

sec1.getParagraphs().add(text1);

//Adicionar um segmento de texto no parágrafo de texto

Segment segment1 = text1.getSegments().add("this is a local link");

//Definir o texto no segmento de texto para ser sublinhado

segment1.getTextInfo().setIsUnderline(true);


//Definir o tipo de link do segmento de texto como Local

//Atribuir o id do parágrafo desejado como um id de destino para o segmento de texto

segment1.getHyperlink().setLinkType(HyperlinkType.Local);

segment1.getHyperlink().setTargetID("product1");

// adicionar uma nova seção que conterá o objeto de texto com ID "Product 1"

Section sec2 = pdf1.getSections().add();

//Criar um parágrafo de texto para ser vinculado ao segmento de texto

Text text3 = new Text(sec1,"product 1 info ...");

//Adicionar o parágrafo de texto à coleção de parágrafos da seção

sec2.getParagraphs().add(text3);

//Definir o id deste segmento de texto para "product1"

text3.setID("product1");


// salvar o arquivo PDF

pdf1.save("UpdateOfCode_Test.pdf");


     }catch(Exception e)

{

System.out.println(e.getMessage());

}
```

## Conclusão

No tópico acima, explicamos algumas das classes e métodos que foram alterados na nova versão. Para uma lista completa de todas as classes e seus membros, por favor, visite [Referência da API Aspose.PDF para Java](http://www.aspose.com/documentation/java-components/aspose.pdf-for-java/aspose.pdf-for-java-api-reference.html)

Para saber mais sobre a Aspose e seus produtos, por favor, clique aqui <http://www.aspose.com/>