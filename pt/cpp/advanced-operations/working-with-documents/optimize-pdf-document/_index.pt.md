---
title: Optimize PDF using C++
linktitle: Optimize PDF
type: docs
weight: 30
url: /cpp/optimize-pdf/
description: Otimize o arquivo PDF, reduza todas as imagens, diminua o tamanho do PDF, remova fontes incorporadas, habilite a reutilização do conteúdo da página, remova ou achate anotações com C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Antes de tudo, qualquer otimização de PDF que você fizer é para o usuário. Em PDFs, a otimização do usuário é principalmente sobre reduzir o tamanho dos seus PDFs para aumentar a velocidade de carregamento deles. Esta é a tarefa mais popular.
Podemos usar várias técnicas para otimizar PDF, mas o mais essencial:

- Otimizar o conteúdo da página para navegação online
- Reduzir ou comprimir todas as imagens
- Habilitar a reutilização do conteúdo da página
- Mesclar fluxos duplicados
- Remover fontes incorporadas
- Remover objetos não utilizados
- Remover campos de formulário achatados
- Remover ou achatar anotações

## Otimizar Documento PDF para a Web

Quando você se depara com a tarefa de otimizar o conteúdo do seu documento PDF para melhor classificação em motores de busca, o Aspose.PDF para C++ tem uma solução.

1. Abra o documento de entrada em um objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Use o método [Optimize](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a04d95824c334f5e543c13f69a19d9cda).
1. Salve o documento otimizado usando o método Save.

O seguinte trecho de código mostra como otimizar um documento PDF para a web.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
//Optimize PDF Document for the Web
void OptimizeForWeb() {
    // String para nome do caminho
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de saída
    String outfilename("OptimizeDocument_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>();

    // Fazer algumas operações (adicionar páginas, imagens, etc)
    // ...

    // Otimizar para web
    document->Optimize();

    // Salvar documento de saída
    document->Save(_dataDir + outfilename);
}
```

## Reduzir Tamanho do PDF

O método [OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) permite reduzir o tamanho do documento eliminando as informações desnecessárias. Por padrão, este método funciona da seguinte forma:

- Recursos que não são usados nas páginas do documento são removidos
- Recursos iguais são unidos em um único objeto
- Objetos não utilizados são deletados

O trecho abaixo é um exemplo. Note, porém, que este método não pode garantir a redução do documento.

```cpp
void ReduceSizePDF() {

    // String para nome do caminho
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de entrada
    String outfilename("ShrinkDocument_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>();
    // Fazer algumas operações (adicionar páginas, imagens, etc.)
    // ...

    // Otimizar documento PDF. Note, porém, que este método não pode garantir a redução do documento
    document->OptimizeResources();

    // Salvar documento de saída
    document->Save(_dataDir + outfilename);
}
```

## Gerenciamento da Estratégia de Otimização

Também podemos personalizar a estratégia de otimização. Atualmente, o método [OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) usa 5 técnicas. Essas técnicas podem ser aplicadas usando o método OptimizeResources() com o parâmetro [OptimizationOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.optimization_options/).

### Encolhendo ou Compactando Todas as Imagens

Para otimizar imagens em seu documento PDF, usaremos [Aspose.Pdf.Optimization](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.optimization).
Para resolver o problema com a otimização de imagens, temos as seguintes opções: reduzir a qualidade da imagem e/ou alterar a resolução delas. Em qualquer caso, [ImageCompressionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options/) deve ser aplicado. No exemplo a seguir, reduzimos as imagens diminuindo [ImageQuality](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a92ee855b042a6b310984b4966ea7154e) para 50.

```cpp
void CompressImage() {
    // String para nome do caminho
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de entrada
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inicializar OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Definir opção CompressImages
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Definir opção ImageQuality
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(50);

    // Otimizar documento PDF usando OptimizationOptions
    document->OptimizeResources(optimizationOptions); 
    // Salvar documento atualizado
    document->Save(_dataDir + outfilename);
}
```
Para definir a imagem em uma resolução mais baixa, defina [ResizeImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a0e5aad7e140ee380c09ebbb8a5238ff6) como verdadeiro e [MaxResolution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a05a4d1ace23ef074b3dc203cb213755e) para o valor correspondente.

```cpp
void ResizeImagesWithLowerResolution() {
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo de entrada
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inicializar OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Definir opção CompressImages
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Definir opção ImageQuality
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // Definir opção ResizeImage
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // Definir opção MaxResolution
    optimizationOptions->get_ImageCompressionOptions()->set_MaxResolution(300);

    // Otimizar documento PDF usando OptimizationOptions
    document->OptimizeResources(optimizationOptions);
    // Salvar documento atualizado
    document->Save(_dataDir + outfilename);
}
```

Aspose.PDF para C++ também oferece controle sobre a configuração em tempo de execução. Hoje, podemos usar dois algoritmos - Padrão e Rápido. Para controlar o tempo de execução, devemos definir uma propriedade [Version](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#aa2f1d93725ce56f8fabe692152bbf3a4).

O trecho a seguir demonstra o algoritmo Rápido:

```cpp
void ResizeImagesWithLowerResolutionFast() {
    auto time = System::DateTime::get_Now().get_Ticks();
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo de entrada
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inicializar OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Definir a opção CompressImages
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Definir a opção ImageQuality
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // Definir a opção ResizeImage
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // Definir a versão de Compressão de Imagem para rápido
    optimizationOptions->get_ImageCompressionOptions()->set_Version (Aspose::Pdf::Optimization::ImageCompressionVersion::Fast);

    // Otimizar documento PDF usando OptimizationOptions
    document->OptimizeResources(optimizationOptions);
    // Salvar documento atualizado
    document->Save(_dataDir + outfilename);
    std::cout << "Ticks: " << System::DateTime::get_Now().get_Ticks() - time << std::endl;
}
```

### Removendo Objetos Não Utilizados

Às vezes, você pode precisar remover alguns objetos não utilizados do seu documento PDF que não são referenciados nas páginas. Isso pode acontecer, por exemplo, quando uma página é removida da árvore de páginas do documento, mas o próprio objeto de página não é removido. Remover esses objetos não torna o documento inválido, mas sim o reduz. Confira o próximo trecho de código:

```cpp
void RemovingUnusedObject() { 
    // String para o caminho do diretório
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo de entrada
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inicializar OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Definir a opção RemoveUsedObject
    optimizationOptions->set_RemoveUnusedObjects(true);

    // Otimizar o documento PDF usando OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Salvar documento atualizado
    document->Save(_dataDir + outfilename); 
}
```

### Removendo Fluxos Não Utilizados

Às vezes, o documento contém fluxos de recursos não utilizados. Esses fluxos não são "objetos não utilizados" porque são referenciados a partir de um dicionário de recursos de página. Assim, eles não são removidos com um método de "remover objetos não utilizados". Mas esses fluxos nunca são usados com o conteúdo da página. Isso pode acontecer em casos quando uma imagem foi removida da página, mas não dos recursos da página. Além disso, essa situação ocorre frequentemente quando páginas são extraídas do documento e as páginas do documento têm recursos "comuns", ou seja, o mesmo objeto Resources. Os conteúdos da página são analisados para determinar se um fluxo de recurso é usado ou não. Fluxos não utilizados são removidos. Isso às vezes diminui o tamanho do documento. O uso dessa técnica é semelhante ao passo anterior: 

```cpp
void RemovingUnusedStreams() { 
    // String para nome do caminho
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de entrada
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>();

    // Inicializar OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Definir opção RemoveUsedStreams
    optimizationOptions->set_RemoveUnusedStreams(true);

    // Otimizar documento PDF usando OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Salvar documento atualizado
    document->Save(_dataDir + outfilename); 
}
```

### Linking Duplicate Streams

Alguns documentos podem conter vários fluxos de recursos duplicados (como imagens, por exemplo). Isso pode acontecer, por exemplo, quando um documento é concatenado com ele mesmo. O documento de saída contém duas cópias independentes do mesmo fluxo de recursos. Analisamos todos os fluxos de recursos e os comparamos. Se os fluxos estão duplicados, eles são mesclados, ou seja, apenas uma cópia é mantida. As referências são alteradas apropriadamente, e as cópias do objeto são removidas. Em alguns casos, isso ajuda a diminuir o tamanho do documento.

```cpp
void LinkingDuplicateStreams() { 
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo de entrada
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inicializar OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Definir opção LinkDuplcateStreams
    optimizationOptions->set_LinkDuplcateStreams(true);

    // Otimizar documento PDF usando OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Salvar documento atualizado
    document->Save(_dataDir + outfilename); 
}
```

Além disso, podemos usar as configurações [AllowReusePageContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.optimization_options#aedaab36eaf8ed5059a2b1e11275bf6d8). Se esta propriedade for definida como true, o conteúdo da página será reutilizado ao otimizar o documento para páginas idênticas.

```cpp
void AllowReusePageContent() { 
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo de entrada
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inicializar OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Definir a opção AllowReusePageContent
    optimizationOptions->set_AllowReusePageContent(true);

    // Otimizar documento PDF usando OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Salvar documento atualizado
    document->Save(_dataDir + outfilename); 
}
```

### Desincorporar Fontes

Quando você cria uma versão PDF do seu arquivo de design pessoal, uma cópia de todas as fontes necessárias é adicionada ao próprio arquivo PDF. Isso é incorporação. Independentemente de onde este PDF seja aberto, seja no seu computador, no computador de um amigo ou no computador do seu provedor de impressão, todas as fontes corretas estarão lá e serão renderizadas corretamente.

Mas, se o documento usa fontes incorporadas, significa que todos os dados das fontes estão armazenados no documento. A vantagem é que o documento é visualizável independentemente de a fonte estar instalada na máquina do usuário ou não. Mas incorporar fontes torna o documento maior. O método de desincorporar fontes remove todas as fontes incorporadas. Assim, o tamanho do documento diminui, mas o próprio documento pode se tornar ilegível se a fonte correta não estiver instalada.

```cpp
void UnembedFonts() {
    // String para nome do caminho
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de entrada
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir+infilename);

    // Inicializar OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Definir opção AllowReusePageContent
    optimizationOptions->set_UnembedFonts(true);

    // Otimizar documento PDF usando OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Salvar documento atualizado
    document->Save(_dataDir + outfilename);
}
```

Os recursos de otimização aplicam esses métodos ao documento. Se algum desses métodos for aplicado, o tamanho do documento provavelmente diminuirá. Se nenhum desses métodos for aplicado, o tamanho do documento não mudará, o que é óbvio.

## Maneiras Adicionais de Reduzir o Tamanho do Documento PDF

### Removendo ou Achatando Anotações

A presença de anotações no seu documento PDF aumenta naturalmente seu tamanho.
As anotações podem ser deletadas quando são desnecessárias. Quando são necessárias mas não requerem edição adicional, podem ser achatadas. Ambas as técnicas reduzirão o tamanho do arquivo.

```cpp
void FlatteningAnnotation() {
    // String para caminho do diretório
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de entrada
    String infilename("OptimizeDocument.pdf");
    // String para nome do arquivo de saída
    String outfilename("OptimizeDocument_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Achar anotações
    for(auto page : document->get_Pages())
    {
        for(auto annotation : page->get_Annotations())
        {
        annotation->Flatten();
        }
    }
    // Salvar documento atualizado
    document->Save(_dataDir + outfilename);
}
```

### Removendo Campos de Formulário

Remover formulários do seu PDF também otimizará seu documento.
Se o documento PDF contiver AcroForms, podemos tentar reduzir o tamanho do arquivo achatando os campos do formulário.

```cpp
void FlatteningFormFields() {
    // String para o caminho do diretório
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo de entrada
    String infilename("OptimizeFormField.pdf");
    // String para o nome do arquivo de saída
    String outfilename("OptimizeFormField_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Aplanar campos de formulário
    // Aplanar Formulários
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for(auto item : document->get_Form()->get_Fields())
        {
            item->Flatten();
        }
    }
    // Salvar documento atualizado
    document->Save(_dataDir + outfilename);
}
```

### Converter um PDF do espaço de cores RGB para tons de cinza

Um arquivo PDF é composto por Texto, Imagem, Anexo, Anotações, Gráficos e outros objetos. Você pode se deparar com a necessidade de converter um PDF do espaço de cores RGB para escala de cinza para que seja mais rápido ao imprimir esses arquivos PDF. Além disso, quando o arquivo é convertido para escala de cinza, o tamanho do documento é reduzido também, mas isso pode causar uma diminuição na qualidade do documento. Este recurso é atualmente suportado pelo recurso Pre-Flight do Adobe Acrobat, mas quando se fala em automação de escritório, Aspose.PDF é uma solução definitiva para fornecer tais vantagens para manipulações de documentos. Para realizar este requisito, o seguinte trecho de código pode ser usado.

```cpp
void ConvertPDFfromColorspaceToGrayscale() {
    // String para nome do caminho
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de entrada
    String infilename("OptimizeDocument.pdf");
    // String para nome do arquivo de saída
    String outfilename("Test-gray_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto strategy = MakeObject<Aspose::Pdf::RgbToDeviceGrayConversionStrategy>();
    for (int idxPage = 1; idxPage <= document->get_Pages()->get_Count(); idxPage++)
    {
        // Obter instância de uma página específica dentro do PDF
        auto page = document->get_Pages()->idx_get(idxPage);
        // Converter a imagem do espaço de cores RGB para o espaço de cores GrayScale
        strategy->Convert(page);
    }
    // Salvar arquivo resultante
    document->Save(_dataDir + outfilename); 
}
```
### Compressão FlateDecode

Aspose.PDF para C++ oferece suporte à compressão FlateDecode para a funcionalidade de otimização de PDF.
Para otimizar a imagem usando a compressão FlateDecode, defina as opções de otimização para Flate.
O trecho de código a seguir mostra como usar a opção em Otimização para armazenar imagens com compressão **FlateDecode**:

```cpp
void FlatDecodeCompression() {
 // String para nome do caminho
 String _dataDir("C:\\Samples\\");

 // String para nome do arquivo de entrada
 String infilename("FlateDecodeCompression.pdf");
 // String para nome do arquivo de saída
 String outfilename("FlateDecodeCompression_out.pdf");

 // Abrir documento
 auto document = MakeObject<Document>(_dataDir + infilename);

 // Inicializar OptimizationOptions
 auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

 // Para otimizar a imagem usando a compressão FlateDecode, defina as opções de otimização para Flate
 optimizationOptions->get_ImageCompressionOptions()->set_Encoding(Aspose::Pdf::Optimization::ImageEncoding::Flate);

 // Otimizar documento PDF usando OptimizationOptions
 document->OptimizeResources(optimizationOptions);

 // Salvar documento atualizado
 document->Save(_dataDir + outfilename);
}
```

### **Armazenar Imagem em XImageCollection**

Aspose.PDF para C++ fornece a capacidade de armazenar novas imagens em [XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection) com compressão FlateDecode. Para habilitar esta opção, você pode usar a flag **ImageFilterType.Flate**.
O trecho de código a seguir mostra como usar esta funcionalidade:

```cpp
void StoreImageInXImageCollection() {

 // String para o nome do caminho
 String _dataDir("C:\\Samples\\");

 // String para o nome do arquivo de saída
 String outfilename("FlateDecodeCompression_out.pdf");

 // Abrir documento
 auto document = MakeObject<Document>();
 
 auto page = document->get_Pages()->Add();
 
 auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.jpg");
 
 page->get_Resources()->get_Images()->Add(imageStream, Aspose::Pdf::ImageFilterType::Flate);
 
 auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

 // Definir coordenadas
 int lowerLeftX = 0;
 int lowerLeftY = 0;
 int upperRightX = 600;
 int upperRightY = 600;
 
 auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

 auto matrix = MakeObject<Matrix>(new double[] {rectangle->get_URX() - rectangle->get_LLX(), 0, 0, rectangle->get_URY() - rectangle->get_LLY(), rectangle->get_LLX(), rectangle->get_LLY()});
 // Usando o operador ConcatenateMatrix (concatenar matriz): define como a imagem deve ser colocada
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

 document->Save(_dataDir + outfilename);
}
```