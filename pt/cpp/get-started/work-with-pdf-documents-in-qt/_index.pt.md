---
title: Trabalhar com Documentos PDF no Qt
type: docs
weight: 130
url: /cpp/work-with-pdf-documents-in-qt/
lastmod: "2021-11-01"
---

Qt é um framework de desenvolvimento de aplicações multiplataforma que permite criar uma variedade de aplicações de desktop, móveis, web e sistemas embarcados. Neste artigo, veremos como você pode integrar nossa biblioteca PDF C++ para trabalhar com documentos PDF em suas aplicações Qt.

## Usando Aspose.PDF para C++ no Qt

Para usar o Aspose.PDF para C++ em sua aplicação Qt no Sistema Operacional Windows, baixe a versão mais recente da API na seção de [downloads](https://downloads.aspose.com/pdf/cpp). Uma vez que a API é baixada, você pode usar uma das seguintes opções para usá-la com o Qt.

- Usando o Qt Creator
- Usando o Visual Studio

Aqui, demonstraremos como integrar e usar o Aspose.PDF para C++ dentro de uma aplicação de console Qt usando o Qt Creator.

### Criar Aplicação de Console Qt

{{% alert color="primary" %}}

Este artigo assume que você instalou corretamente o ambiente de desenvolvimento Qt e o Qt Creator.

{{% /alert %}}

- Abra o Qt Creator e crie um novo *Qt Console Application*.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application.jpg)

- Selecione a opção QMake no dropdown do *Build System*.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application-QMake.jpg)

- Selecione o kit apropriado e finalize o assistente.

Neste ponto, você deve ter uma aplicação executável Qt Console Application que deve compilar sem problemas.

### Integrar a API Aspose.PDF para C++ com Qt

- Extraia o arquivo Aspose.PDF para C++ que você baixou anteriormente
- Copie as pastas *Aspose.Pdf.Cpp* e *CodePorting.Native.Cs2Cpp_vc14_20.4* do pacote extraído do Aspose.PDF para C++ para a raiz do projeto. Seu projeto deve se parecer com a imagem a seguir.

![todo:image_alt_text](work-with-pdf-documents-in-qt_1.png)

- Para adicionar caminhos para as pastas lib e include, clique com o botão direito no projeto no painel LHS e selecione *Add Library*.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library.jpg)

- Selecione a opção Biblioteca Externa e navegue pelos caminhos para incluir e lib pastas uma por uma.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library-2.jpg)

- Uma vez feito, seu arquivo de projeto .pro conterá as seguintes entradas:

![todo:image_alt_text](work-with-pdf-documents-in-qt_2.png)

- Compile a aplicação e você terá concluído a integração.

### Criar Documento PDF no Qt

Agora que o Aspose.PDF para C++ foi integrado ao Qt, estamos prontos para criar um documento PDF com algum texto e salvá-lo no disco. Para fazer isso:

- Inclua os seguintes cabeçalhos em main.cpp

```cpp

    #include "Aspose.PDF.Cpp/Document.h"
    #include "Aspose.PDF.Cpp/Page_.h"
    #include "Aspose.PDF.Cpp/PageCollection.h"
    #include "Aspose.PDF.Cpp/Generator/Paragraphs.h"
    #include "Aspose.PDF.Cpp/Text/TextFragment.h"
```

- Insira o seguinte código na função principal para gerar um documento PDF e salvar no disco

```cpp

    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Text;
    
    QString text = "Olá Mundo";
    auto doc = MakeObject<Document>();

    auto pages = doc->get_Pages();

    pages->Add();

    auto page = pages->idx_get(1);

    auto paragraps = page->get_Paragraphs();

    paragraps->Add(MakeObject<TextFragment>(text.toStdU16String().c_str()));

    doc->Save(file_name.toStdU16String().c_str());
```