---
title: Migração da versão anterior a 4.x.x do Aspose.PDF para Java
type: docs
weight: 20
url: pt/java/migration-from-pre-4-x-x-version-of-aspose-pdf-for-java/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Uma nova versão auto-portada do Aspose.PDF para Java foi lançada e agora este único produto suporta a capacidade de gerar documentos PDF do zero, bem como fornece a capacidade de manipular documentos PDF existentes.

{{% /alert %}}

## Binários do produto

{{% alert color="primary" %}}

Na primeira versão lançada (v4.0.0), estamos enviando dois arquivos jar, ou seja, **aspose.pdf-3.3.0.jdk15.jar** e **aspose.pdf-new-4.0.0.jar**.

- **aspose.pdf-3.3.0.jdk14.jar**

Este arquivo jar é a mesma versão do produto atualmente disponível no módulo de download com o título [Aspose.PDF for java 3.3.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry417659.aspx). Daqui em diante, vamos chamar esta versão de lançamento como Aspose.PDF para Java legado. Neste primeiro lançamento, os usuários existentes do Aspose.PDF para Java podem não ser impactados porque eles recebem a mesma versão de lançamento. No entanto, em breve, removeremos este arquivo jar separado e todas as classes e enumerações do Aspose.PDF para Java legado (pré 4.x.x) estarão disponíveis sob o pacote com.aspose.pdf.generator do único arquivo aspose.pdf-new-4.x.x.jar.

- **aspose.pdf-new-4.0.0.jar**  
  Este arquivo jar é uma nova versão auto-portada do Aspose.PDF para .NET para a plataforma Java.
 Este arquivo jar contém o novo Modelo de Objeto de Documento (DOM) para criar e também manipular arquivos PDF existentes, além do atual Aspose.PDF.Kit para Java. Todas as classes e enumerações do Aspose.PDF.Kit para Java estão agrupadas no pacote com.aspose.pdf.facades e no terceiro trimestre de 2013, o Aspose.PDF.Kit para Java será descontinuado. Portanto, incentivamos nossos clientes atuais do Aspose.PDF.Kit para Java a tentar migrar seu código para a nova versão auto-portada.

Por favor, confira a seguinte postagem no blog para obter mais informações sobre a Estrutura do Aspose.PDF autoportado para Java.
{{% /alert %}}