---
title: Adicionar Número de Página ao PDF com C++
linktitle: Adicionar Número de Página
type: docs
weight: 100
url: /cpp/add-page-number/
description: Aspose.PDF para C++ permite adicionar Carimbo de Número de Página ao seu arquivo PDF usando a classe PageNumber Stamp.
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Como Adicionar Números de Página a um PDF Existente

Todos os documentos devem ter números de página. O número de página facilita para o leitor localizar diferentes partes do documento.
**Aspose.PDF para C++** permite que você adicione números de página com PageNumberStamp.

Os seguintes passos e código de exemplo ilustram como adicionar etiquetas de numeração de página a um documento PDF existente usando o elemento de página [PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp) para adicionar automaticamente números de página a um PDF.

Passos para Adicionar Números de Página a um Documento PDF Existente:

Para adicionar um carimbo de número de página, você precisa criar um objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) e um objeto [PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp) usando as propriedades necessárias.

Após isso, você pode chamar o método [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) da [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) para adicionar o carimbo no PDF.

Você também pode definir os atributos de fonte do carimbo de número de página.

O trecho de código a seguir mostra como adicionar números de página em um arquivo PDF.

```cpp
void AddPageNumberToPDF() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("PageNumberStamp.pdf");
    String outputFileName("PageNumberStamp_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Criar carimbo de número de página
    auto pageNumberStamp = MakeObject<PageNumberStamp>();
    //// Se o carimbo é de fundo
    //pageNumberStamp.Background = false;
    //pageNumberStamp.Format = "Página # de " + pdfDocument.Pages.Count;
    //pageNumberStamp.BottomMargin = 10;
    //pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
    //pageNumberStamp.StartingNumber = 1;

    //// Definir propriedades do texto
    //pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
    //pageNumberStamp.TextState.FontSize = 14.0F;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
    //pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

    // Adicionar carimbo a uma página específica
    document->get_Pages()->idx_get(1)->AddStamp(pageNumberStamp);

    // Salvar documento de saída
    document->Save(_dataDir+ outputFileName);
}
```

## Exemplo Ao Vivo

[Adicionar números de página em PDF](https://products.aspose.app/pdf/page-number) é um aplicativo web gratuito online que permite investigar como a funcionalidade de adicionar números de página funciona.

[![Como adicionar número de página em pdf usando C++](page_number.png)](https://products.aspose.app/pdf/page-number)

## Adicionar/Remover numeração Bates

**Numeração Bates** (também conhecida como carimbo Bates) é usada nos campos jurídico, médico e empresarial para colocar números de identificação e/ou marcas de data/hora em imagens e documentos à medida que são digitalizados ou processados, por exemplo, durante a fase de descoberta de preparações para julgamento ou identificação de recibos comerciais. Este processo fornece identificação, proteção e numeração consecutiva automática das imagens ou documentos.

Aspose.PDF tem suporte limitado para Numeração Bates por enquanto. Esta funcionalidade será atualizada de acordo com as solicitações dos clientes.

### Como remover a numeração Bates

```cpp
void WorkingWithPages::RemoveBatesNubmering()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("BatesNumbering.pdf");
    String outputFileName("BatesNumbering_out.pdf");
    String customSubtype("BatesN");
    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    for (auto page : document->get_Pages())
    {
        auto coll = page->get_Artifacts();
        for (auto batesNum : coll)
        {
        if (batesNum->get_CustomSubtype() == customSubtype)
            page->get_Artifacts()->Delete(batesNum);
        }
    }

    // Salvar documento de saída
    document->Save(_dataDir + outputFileName);
}
```