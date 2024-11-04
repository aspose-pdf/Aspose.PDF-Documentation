---
title: Como assinar digitalmente PDF
linktitle: Assinar digitalmente PDF
type: docs
weight: 10
url: /cpp/digitally-sign-pdf-file/
description: Assine digitalmente documentos PDF usando C++. Verifique ou valide PDFs assinados digitalmente usando C++.
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Assinar PDF com assinaturas digitais

Você pode assinar o documento PDF para confirmar seu conteúdo ou pode aprovar o documento com Aspose.PDF.

Aspose.PDF para C++ suporta o recurso de assinar digitalmente os arquivos PDF usando a classe SignatureField. Você também pode certificar um arquivo PDF com um Certificado PKCS12. Algo semelhante a [Adicionar assinaturas e segurança no Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

Use a classe [PdfFileSignature](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_signature) para assinar seu PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SecuringAndSigning::SignDocument() {

// String para nome do caminho.

String _dataDir("C:\\Samples\\");


String inFile = _dataDir + u"DigitallySign.pdf";

String outFile = _dataDir + u"DigitallySign_out.pdf";


auto document = MakeObject<Document>(inFile);


auto signature = MakeObject<PdfFileSignature>(document);


auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020"); // Use PKCS7/PKCS7Detached
























// objetos

System::Drawing::Rectangle rect(300, 100, 400, 200);

signature->Sign(1, true, rect, pkcs);

// Salvar arquivo PDF de saída

signature->Save(outFile);
}
```

## Adicionar carimbo de data/hora à assinatura digital

### Como assinar digitalmente um PDF com carimbo de data/hora

Aspose.PDF para C++ suporta a assinatura digital do PDF com um servidor de carimbo de data/hora ou serviço Web.

Carimbos de data/hora são usados para indicar a data e a hora em que você assinou o documento. A marcação de tempo confiável prova que o conteúdo dos seus PDFs existia em um ponto específico no tempo e não foi alterado desde então.

Use a classe [TimestampSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.timestamp_settings) para adicionar um carimbo de tempo confiável a assinaturas digitais ou documentos.

Por favor, veja o trecho de código a seguir que obtém o carimbo de data/hora e o adiciona ao documento PDF:

```cpp
void SecuringAndSigning::SignWithTimeStampServer() {


// String para nome do caminho.

String _dataDir("C:\\Samples\\");

auto document = MakeObject<Document>(_dataDir + u"SimpleResume.pdf");

auto signature = MakeObject<PdfFileSignature>(document);


auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020");


auto timestampSettings = MakeObject<TimestampSettings>(u"https://freetsa.org/tsr", String::Empty); // Usuário/Senha podem
























// ser omitidos

pkcs->set_TimestampSettings(timestampSettings);


System::Drawing::Rectangle rect(100, 100, 200, 100);

// Crie qualquer um dos três tipos de assinatura

signature->Sign(1, u"Motivo da Assinatura", u"Contato", u"Localização", true, rect, pkcs);

// Salve o arquivo PDF de saída

signature->Save(_dataDir + u"DigitallySignWithTimeStamp_out.pdf");
}
```