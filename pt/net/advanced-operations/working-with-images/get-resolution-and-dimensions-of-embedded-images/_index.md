---
title: Obter Resolução e Dimensões de Imagens
linktitle: Obter Resolução e Dimensões
type: docs
weight: 40
url: /pt/net/get-resolution-and-dimensions-of-embedded-images/
description: Esta seção mostra detalhes sobre como obter a resolução e as dimensões de Imagens Incorporadas
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Obter Resolução e Dimensões de Imagens",
    "alternativeHeadline": "Como obter Resolução e Dimensões de Imagens Incorporadas",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos em PDF",
    "keywords": "pdf, c#, obter resolução, obter dimensões",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/get-resolution-and-dimensions-of-embedded-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-resolution-and-dimensions-of-embedded-images/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta seção mostra detalhes sobre como obter a resolução e as dimensões de Imagens Incorporadas"
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

Este tópico explica como usar as classes de operador no espaço de nomes Aspose.PDF que fornecem a capacidade de obter informações de resolução e dimensão sobre imagens sem a necessidade de extraí-las.

Existem diferentes maneiras de alcançar isso. Este artigo explica como usar uma `arraylist` e [classes de colocação de imagens](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement).

1. Primeiro, carregue o arquivo PDF fonte (com imagens).
1. Em seguida, crie um objeto ArrayList para armazenar os nomes de quaisquer imagens no documento.
1. Obtenha as imagens usando a propriedade Page.Resources.Images.
1. Crie um objeto stack para manter o estado gráfico da imagem e use-o para acompanhar diferentes estados de imagem.
1.
1.
1. Como podemos modificar a matriz com ConcatenateMatrix, também podemos precisar voltar ao estado original da imagem. Use os operadores GSave e GRestore. Esses operadores são emparelhados e devem ser chamados juntos. Por exemplo, se você realizar algum trabalho gráfico com transformações complexas e finalmente retornar as transformações para o estado inicial, a abordagem será algo assim:

```csharp
// Desenhar algum texto
GSave

ConcatenateMatrix  // rotaciona o conteúdo após o operador

// Algum trabalho gráfico

ConcatenateMatrix // escala (com a rotação anterior) o conteúdo após o operador

// Algum outro trabalho gráfico

GRestore

// Desenhar algum texto
```

Como resultado, o texto é desenhado de forma regular, mas algumas transformações são realizadas entre os operadores de texto. Para exibir a imagem ou para desenhar objetos de forma e imagens, precisamos usar o operador Do.

Também temos uma classe chamada XImage que oferece duas propriedades, Width e Height, que podem ser usadas para obter as dimensões da imagem.
1.
1. Exiba as informações em um Prompt de Comando junto com o nome da imagem.

O seguinte trecho de código mostra como obter as dimensões e a resolução de uma imagem sem extrair a imagem do documento PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Carregar o arquivo PDF fonte
Document doc = new Document(dataDir+ "ImageInformation.pdf");

// Definir a resolução padrão para imagem
int defaultResolution = 72;
System.Collections.Stack graphicsState = new System.Collections.Stack();
// Definir o objeto de lista de array que conterá os nomes das imagens
System.Collections.ArrayList imageNames = new System.Collections.ArrayList(doc.Pages[1].Resources.Images.Names);
// Inserir um objeto na pilha
graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

// Obter todos os operadores na primeira página do documento
foreach (Operator op in doc.Pages[1].Contents)
{
    // Usar os operadores GSave/GRestore para reverter as transformações para o estado anteriormente definido
    Aspose.Pdf.Operators.GSave opSaveState = op as Aspose.Pdf.Operators.GSave;
    Aspose.Pdf.Operators.GRestore opRestoreState = op as Aspose.Pdf.Operators.GRestore;
    // Instanciar o objeto ConcatenateMatrix, pois ele define a matriz de transformação atual.
    Aspose.Pdf.Operators.ConcatenateMatrix opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
    // Criar o operador Do que desenha objetos dos recursos. Ele desenha objetos Form e objetos Image
    Aspose.Pdf.Operators.Do opDo = op as Aspose.Pdf.Operators.Do;

    if (opSaveState != null)
    {
        // Salvar o estado anterior e empurrar o estado atual para o topo da pilha
        graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
    }
    else if (opRestoreState != null)
    {
        // Descartar o estado atual e restaurar o anterior
        graphicsState.Pop();
    }
    else if (opCtm != null)
    {
        System.Drawing.Drawing2D.Matrix cm = new System.Drawing.Drawing2D.Matrix(
           (float)opCtm.Matrix.A,
           (float)opCtm.Matrix.B,
           (float)opCtm.Matrix.C,
           (float)opCtm.Matrix.D,
           (float)opCtm.Matrix.E,
           (float)opCtm.Matrix.F);

        // Multiplicar a matriz atual com a matriz de estado
        ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);

        continue;
    }
    else if (opDo != null)
    {
        // Caso este seja um operador de desenho de imagem
        if (imageNames.Contains(opDo.Name))
        {
            System.Drawing.Drawing2D.Matrix lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
            // Criar objeto XImage para conter imagens da primeira página do pdf
            XImage image = doc.Pages[1].Resources.Images[opDo.Name];

            // Obter dimensões da imagem
            double scaledWidth = Math.Sqrt(Math.Pow(lastCTM.Elements[0], 2) + Math.Pow(lastCTM.Elements[1], 2));
            double scaledHeight = Math.Sqrt(Math.Pow(lastCTM.Elements[2], 2) + Math.Pow(lastCTM.Elements[3], 2));
            // Obter informações de Altura e Largura da imagem
            double originalWidth = image.Width;
            double originalHeight = image.Height;

            // Calcular resolução com base nas informações acima
            double resHorizontal = originalWidth * defaultResolution / scaledWidth;
            double resVertical = originalHeight * defaultResolution / scaledHeight;

            // Exibir informações de Dimensão e Resolução de cada imagem
            Console.Out.WriteLine(
                    string.Format(dataDir + "imagem {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                                 opDo.Name, scaledWidth, scaledHeight, resHorizontal,
                                 resVertical));
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de Manipulação de PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

