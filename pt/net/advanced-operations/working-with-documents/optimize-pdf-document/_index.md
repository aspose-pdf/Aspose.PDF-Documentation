---
title: Otimizar, Comprimir ou Reduzir o Tamanho de PDF em C#
linktitle: Otimizar PDF
type: docs
weight: 30
url: /pt/net/optimize-pdf/
description: Otimizar arquivo PDF, reduzir todas as imagens, diminuir o tamanho do PDF, desincorporar fontes, remover objetos não utilizados com C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Otimizar PDF usando C#",
    "alternativeHeadline": "Como otimizar PDF com .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, otimizar pdf",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/optimize-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Otimizar arquivo PDF, reduzir todas as imagens, diminuir o tamanho do PDF, desincorporar fontes, remover objetos não utilizados com C#."
}
</script>

Um documento PDF pode às vezes conter dados adicionais. Reduzir o tamanho de um arquivo PDF ajudará a otimizar a transferência de rede e o armazenamento. Isso é especialmente útil para publicação em páginas da web, compartilhamento em redes sociais, envio por e-mail ou arquivamento em armazenamento. Podemos usar várias técnicas para otimizar o PDF:

- Otimizar o conteúdo da página para navegação online
- Reduzir ou comprimir todas as imagens
- Habilitar a reutilização do conteúdo da página
- Mesclar fluxos duplicados
- Desincorporar fontes
- Remover objetos não utilizados
- Remover campos de formulário achatados
- Remover ou achatar anotações

{{% alert color="primary" %}}

 A explicação detalhada dos métodos de otimização pode ser encontrada na página Visão Geral dos Métodos de Otimização.

{{% /alert %}}

## Otimizar Documento PDF para a Web

Otimização, ou linearização para a Web, refere-se ao processo de tornar um arquivo PDF adequado para navegação online usando um navegador web. Para otimizar um arquivo para exibição na web:

1. Abra o documento de entrada em um objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1.
1.
1. Salve o documento otimizado usando o método [Salvar](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save).

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

O seguinte trecho de código mostra como otimizar um documento PDF para a web.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");

// Otimizar para web
pdfDocument.Optimize();

dataDir = dataDir + "OptimizeDocument_out.pdf";

// Salvar documento de saída
pdfDocument.Save(dataDir);
```

## Reduzir Tamanho do PDF

O método [OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) permite reduzir o tamanho do documento eliminando informações desnecessárias.
O método [OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) permite reduzir o tamanho do documento eliminando informações desnecessárias.

- Recursos que não são usados nas páginas do documento são removidos
- Recursos iguais são unidos em um único objeto
- Objetos não utilizados são deletados

O trecho abaixo é um exemplo. Note, porém, que este método não pode garantir a redução do documento.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Abrir documento
Document pdfDocument = new Document(dataDir + "ShrinkDocument.pdf");
// Otimizar documento PDF. Note, porém, que este método não pode garantir a redução do documento
pdfDocument.OptimizeResources();
dataDir = dataDir + "ShrinkDocument_out.pdf";
// Salvar documento atualizado
pdfDocument.Save(dataDir);
```

## Gestão da Estratégia de Otimização

Também podemos personalizar a estratégia de otimização.
Também podemos personalizar a estratégia de otimização.

### Reduzindo ou Comprimindo Todas as Imagens

Temos duas maneiras de trabalhar com imagens: reduzir a qualidade da imagem e/ou mudar sua resolução. Em qualquer caso, [ImageCompressionOptions](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions) deve ser aplicado. No exemplo a seguir, reduzimos as imagens ao diminuir [ImageQuality](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality) para 50.

`ImageQuality` funciona de maneira semelhante à qualidade JPEG, onde o valor 0 é o mais baixo e o valor 100 é o mais alto.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Abrir documento
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// Inicializar OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Definir opção CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Definir opção ImageQuality
optimizeOptions.ImageCompressionOptions.ImageQuality = 50;
// Otimizar documento PDF usando OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "Shrinkimage_out.pdf";
// Salvar documento atualizado
pdfDocument.Save(dataDir);
```
Outra maneira é redimensionar as imagens para uma resolução menor. Nesse caso, devemos definir ResizeImages como verdadeiro e MaxResolution para o valor apropriado.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Inicializar Tempo
var time = DateTime.Now.Ticks;
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Abrir documento
Document pdfDocument = new Document(dataDir + "ResizeImage.pdf");
// Inicializar OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Definir opção CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Definir opção ImageQuality
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// Definir opção ResizeImage
optimizeOptions.ImageCompressionOptions.ResizeImages = true;
// Definir opção MaxResolution
optimizeOptions.ImageCompressionOptions.MaxResolution = 300;
// Otimizar documento PDF usando OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "ResizeImages_out.pdf";
// Salvar documento atualizado
pdfDocument.Save(dataDir);
```
Outra questão importante é o tempo de execução. Mas, novamente, podemos gerenciar essa configuração também. Atualmente, podemos usar dois algoritmos - Padrão e Rápido. Para controlar o tempo de execução, devemos definir uma propriedade [Versão](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/version). O seguinte trecho demonstra o algoritmo Rápido:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá até https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Inicializar Tempo
var time = DateTime.Now.Ticks;
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Abrir documento
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// Inicializar OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Definir a opção CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Definir a opção de Qualidade de Imagem
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// Definir a Versão de Compressão de Imagem para rápido
optimizeOptions.ImageCompressionOptions.Version = Pdf.Optimization.ImageCompressionVersion.Fast;
// Otimizar o documento PDF usando OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "FastShrinkImages_out.pdf";
// Salvar o documento atualizado
pdfDocument.Save(dataDir);
Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
```
### Removendo Objetos Não Utilizados

Um documento PDF às vezes contém objetos PDF que não são referenciados por nenhum outro objeto no documento. Isso pode acontecer, por exemplo, quando uma página é removida da árvore de páginas do documento, mas o objeto da página em si não é removido. Remover esses objetos não invalida o documento, mas sim reduz seu tamanho.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Abrir documento
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Configurar a opção RemoveUsedObject
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedObjects = true
};
// Otimizar o documento PDF usando OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Salvar o documento atualizado
pdfDocument.Save(dataDir);
```

### Removendo Streams Não Utilizados

Às vezes, o documento contém streams de recursos não utilizados.
Às vezes, o documento contém fluxos de recursos não utilizados.

```csharp
// Para exemplos completos e arquivos de dados, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Abrir documento
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Configurar a opção RemoveUsedStreams
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedStreams = true
};
// Otimizar o documento PDF usando OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Salvar o documento atualizado
pdfDocument.Save(dataDir);
```

### Vinculando Fluxos Duplicados

Alguns documentos podem conter vários fluxos de recursos idênticos (como imagens, por exemplo).
Alguns documentos podem conter vários fluxos de recursos idênticos (como imagens, por exemplo).

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Abrir documento
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Definir a opção LinkDuplicateStreams
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    LinkDuplicateStreams = true
};
// Otimizar documento PDF usando OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Salvar documento atualizado
pdfDocument.Save(dataDir);
```

Adicionalmente, podemos usar as configurações [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent).
Adicionalmente, podemos usar as configurações [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent).

```csharp
// Para exemplos completos e arquivos de dados, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Abrir documento
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Definir a opção AllowReusePageContent
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    AllowReusePageContent = true
};
Console.WriteLine("Início");
// Otimizar o documento PDF usando OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
// Salvar o documento atualizado
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Concluído");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Tamanho do arquivo original: {0}. Tamanho do arquivo reduzido: {1}", fi1.Length, fi2.Length);
```
### Desincorporando Fontes

Se o documento usa fontes incorporadas, significa que todos os dados da fonte estão armazenados no documento. A vantagem é que o documento pode ser visualizado independentemente de a fonte estar instalada na máquina do usuário ou não. Mas incorporar fontes torna o documento maior. O método de desincorporar fontes remove todas as fontes incorporadas. Assim, o tamanho do documento diminui, mas o próprio documento pode se tornar ilegível se a fonte correta não estiver instalada.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Abrir documento
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Configurar opção UnembedFonts
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    UnembedFonts = true
};
Console.WriteLine("Início");
// Otimizar documento PDF usando OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
// Salvar documento atualizado
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Concluído");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Tamanho do arquivo original: {0}. Tamanho do arquivo reduzido: {1}", fi1.Length, fi2.Length);
```
Os recursos de otimização aplicam esses métodos ao documento. Se algum desses métodos for aplicado, o tamanho do documento provavelmente diminuirá. Se nenhum desses métodos for aplicado, o tamanho do documento não mudará, o que é óbvio.

## Métodos Adicionais para Reduzir o Tamanho do Documento PDF

### Removendo ou Achatando Anotações

Anotações podem ser deletadas quando são desnecessárias. Quando são necessárias, mas não requerem edição adicional, podem ser achatadas. Ambas as técnicas reduzirão o tamanho do arquivo.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Abrir documento
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Achatar anotações
foreach (var page in pdfDocument.Pages)
{
    foreach (var annotation in page.Annotations)
    {
        annotation.Flatten();
    }

}
// Salvar documento atualizado
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
```
### Removendo Campos de Formulários

Se o documento PDF contém AcroForms, podemos tentar reduzir o tamanho do arquivo achatando os campos de formulário.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Carregar o formulário PDF de origem
Document doc = new Document(dataDir + "input.pdf");

// Achatar os Formulários
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// Salvar o documento atualizado
doc.Save(dataDir);
```

### Converter um PDF do espaço de cores RGB para escala de cinzas

Um arquivo PDF é composto por Texto, Imagem, Anexo, Anotações, Gráficos e outros objetos.
Um arquivo PDF é composto por Texto, Imagem, Anexo, Anotações, Gráficos e outros objetos.

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Carregar o arquivo PDF de origem
using (Document document = new Document(dataDir + "input.pdf"))
{
    Aspose.Pdf.RgbToDeviceGrayConversionStrategy strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();
    for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
    {
        // Obter instância de uma página específica dentro do PDF
        Page page = document.Pages[idxPage];
        // Converter a imagem do espaço de cores RGB para o espaço de cores em escala de cinza
        strategy.Convert(page);
    }
    // Salvar o arquivo resultante
    document.Save(dataDir + "Test-gray_out.pdf");
}
```

### Compressão FlateDecode

{{% alert color="primary" %}}

Este recurso é suportado pela versão 18.12 ou superior.

{{% /alert %}}

Aspose.PDF para .NET oferece suporte à compressão FlateDecode para a funcionalidade de Otimização de PDF.
Aspose.PDF para .NET oferece suporte à compressão FlateDecode para a funcionalidade de Otimização de PDF.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-FlateDecodeCompression-1.cs" >}}

### **Armazenar Imagem em XImageCollection**

Aspose.PDF para .NET oferece a capacidade de armazenar novas imagens em **XImageCollection** com compressão FlateDecode. Para habilitar esta opção, você pode usar a bandeira **ImageFilterType.Flate**. O seguinte trecho de código mostra como usar essa funcionalidade:

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-StoreImageInXImageCollection-1.cs" >}}

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
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
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


