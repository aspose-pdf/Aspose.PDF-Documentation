---
title: Adicionar Imagem ao PDF usando C#
linktitle: Adicionar Imagem
type: docs
weight: 10
url: pt/net/add-image-to-existing-pdf-file/
description: Esta seção descreve como adicionar imagem a um arquivo PDF existente usando a biblioteca C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Imagem ao PDF usando C#",
    "alternativeHeadline": "Como adicionar Imagem ao PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento PDF",
    "keywords": "pdf, c#, adicionar imagem ao pdf",
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
    "url": "/net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta seção descreve como adicionar imagem a um arquivo PDF existente usando a biblioteca C#."
}
</script>
## Adicionar Imagem em um Arquivo PDF Existente

Cada página de um PDF contém propriedades de Recursos e Conteúdos. Recursos podem ser imagens e formulários, por exemplo, enquanto o conteúdo é representado por um conjunto de operadores PDF. Cada operador tem seu nome e argumento. Este exemplo usa operadores para adicionar uma imagem a um arquivo PDF.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Para adicionar uma imagem a um arquivo PDF existente:

- Crie um objeto Document e abra o documento PDF de entrada.
- Obtenha a página na qual você deseja adicionar uma imagem.
- Adicione a imagem à coleção de Recursos da página.
- Use operadores para posicionar a imagem na página:
- Use o operador GSave para salvar o estado gráfico atual.
- Use o operador ConcatenateMatrix para especificar onde a imagem será colocada.
- Use o operador Do para desenhar a imagem na página.
- Finalmente, use o operador GRestore para salvar o estado gráfico atualizado.
- Salve o arquivo.
O seguinte trecho de código mostra como adicionar a imagem em um documento PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Abrir documento
Document pdfDocument = new Document(dataDir+ "AddImage.pdf");

// Definir coordenadas
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Obter a página onde a imagem precisa ser adicionada
Page page = pdfDocument.Pages[1];
// Carregar imagem em stream
FileStream imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open);
// Adicionar imagem à coleção de Imagens dos Recursos da Página
page.Resources.Images.Add(imageStream);
// Usando o operador GSave: este operador salva o estado gráfico atual
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// Criar objetos Retângulo e Matriz
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// Usando o operador ConcatenateMatrix (concatenar matriz): define como a imagem deve ser colocada
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// Usando o operador Do: este operador desenha a imagem
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// Usando o operador GRestore: este operador restaura o estado gráfico
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "AddImage_out.pdf";
// Salvar documento atualizado
pdfDocument.Save(dataDir);
```
{{% alert color="primary" %}}

Por padrão, a qualidade JPEG é definida para 100%. Para aplicar uma compressão e qualidade melhores, use as seguintes sobrecargas:

{{% /alert %}}

- a sobrecarga do método Replace foi adicionada na classe XImageCollection: public void Replace(int index, Stream stream, int quality)
- a sobrecarga do método Add foi adicionada na classe XImageCollection: public void Add(Stream stream, int quality)

## Adicionar Imagem em um Arquivo PDF Existente (Facades)

Existe também uma alternativa, maneira mais fácil de adicionar uma Imagem a um arquivo PDF.
Existe também uma alternativa mais fácil para adicionar uma Imagem a um arquivo PDF.

```csharp
string imageFileName = Path.Combine(_dataDir, "Images", "Sample-01.jpg");
string outputPdfFileName = Path.Combine(_dataDir, "Example-add-image-mender.pdf");
Document document = new Document();
Page page = document.Pages.Add();
page.SetPageSize(PageSize.A3.Height, PageSize.A3.Width);
page = document.Pages.Add();
Aspose.Pdf.Facades.PdfFileMend mender = new Aspose.Pdf.Facades.PdfFileMend(document);
mender.AddImage(imageFileName, 1, 0, 0, (float)page.CropBox.Width, (float)page.CropBox.Height);
document.Save(outputPdfFileName);
```

## Colocar imagem na página e preservar (controlar) a proporção

Se não conhecemos as dimensões da imagem, há sempre a chance de obter uma imagem distorcida na página. O exemplo a seguir mostra uma das maneiras de evitar isso.

```csharp
public static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    var bitmap = System.Drawing.Image.FromFile(_dataDir + "3410492.jpg");

    int width;
    int height;

    width = bitmap.Width;
    height = bitmap.Height;

    var document = new Aspose.Pdf.Document();

    var page = document.Pages.Add();

    int scaledWidth = 400;
    int scaledHeight = scaledWidth * height / width;

    page.AddImage(_dataDir + "3410492.jpg", new Aspose.Pdf.Rectangle(10, 10, scaledWidth, scaledHeight));
    document.Save(_dataDir + "sample_image.pdf");
}
```
## Identificar se a imagem dentro do PDF é Colorida ou Preto e Branco

Diferentes tipos de compressão podem ser aplicados às imagens para reduzir seu tamanho. O tipo de compressão aplicada depende do espaço de cor da imagem original, ou seja, se a imagem for Colorida (RGB), então a compressão JPEG2000 deve ser aplicada, e se for Preto e Branco, então deve-se aplicar a compressão JBIG2/JBIG2000. Portanto, identificar cada tipo de imagem e usar um tipo apropriado de compressão criará uma saída melhor/otimizada.

Um arquivo PDF pode conter elementos como Texto, Imagem, Gráfico, Anexo, Anotação etc, e se o arquivo PDF original contiver imagens, podemos determinar o espaço de cor da imagem e aplicar a compressão apropriada para reduzir o tamanho do arquivo PDF. O seguinte trecho de código mostra os passos para Identificar se a imagem dentro do PDF é Colorida ou Preto e Branco.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Contador para imagens em escala de cinza
int grayscaled = 0;
// Contador para imagens RGB
int rgd = 0;

using (Document document = new Document(dataDir + "ExtractImages.pdf"))
{
    foreach (Page page in document.Pages)
    {
        Console.WriteLine("--------------------------------");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
        page.Accept(abs);
        // Obter a contagem de imagens em uma página específica
        Console.WriteLine("Total de Imagens = {0} na página número {1}", abs.ImagePlacements.Count, page.Number);
        // Document.Pages[29].Accept(abs);
        int image_counter = 1;
        foreach (ImagePlacement ia in abs.ImagePlacements)
        {
            ColorType colorType = ia.Image.GetColorType();
            switch (colorType)
            {
                case ColorType.Grayscale:
                    ++grayscaled;
                    Console.WriteLine("Imagem {0} é Escala de Cinza...", image_counter);
                    break;
                case ColorType.Rgb:
                    ++rgd;
                    Console.WriteLine("Imagem {0} é RGB...", image_counter);
                    break;
            }
            image_counter += 1;
        }
    }
}
```
## Controlar a Qualidade da Imagem

É possível controlar a qualidade de uma imagem que está sendo adicionada a um arquivo PDF. Use o método [Replace](https://reference.aspose.com/pdf/net/aspose.pdf.ximagecollection/replace/methods/1) sobrecarregado na classe [XImageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/ximagecollection).

O seguinte trecho de código demonstra como converter todas as imagens do documento em JPEGs que usam 80% de qualidade para compressão.

```csharp
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document(inFile);
foreach (Aspose.PDF.Page page in pdfDocument.Pages)
{
    int idx = 1;
    foreach (Aspose.PDF.XImage image in page.Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
            page.Resources.Images.Replace(idx, imageStream, 80);
            idx = idx + 1;
        }
    }
}

// pdfDocument.OptimizeResources();

pdfDocument.Save(outFile);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para a Biblioteca .NET",
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

