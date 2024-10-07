---

title: Rotating stamp about the center point

type: docs

weight: 10

url: /net/rotating-stamp-about-the-center-point/

description: Esta seção explica como girar o carimbo em torno do ponto central usando a classe Stamp.

lastmod: "2021-06-05"

draft: false

---

{{% alert color="primary" %}}

O [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) no [Aspose.PDF para .NET](/pdf/net/) permite que você adicione um carimbo em um arquivo PDF existente. Às vezes, os usuários precisam girar o carimbo. Neste artigo, veremos como girar um carimbo em torno de seu ponto central.

{{% /alert %}}

## Detalhes da implementação

A classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) permite que você adicione uma marca d'água em um arquivo PDF. Você pode especificar a imagem a ser adicionada como um carimbo usando o método [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/bindimage/methods/1). O método [SetOrigin](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setorigin) permite que você defina a origem do carimbo adicionado; esta origem são as coordenadas inferiores esquerdas do carimbo. Você também pode definir o tamanho da imagem usando o método [SetImageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setimagesize).

Agora, vemos como o carimbo pode ser rotacionado em torno do centro do carimbo. [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class fornece uma propriedade chamada Rotation. Esta propriedade define ou obtém a rotação de 0 a 360 do conteúdo do carimbo. Podemos especificar qualquer valor de rotação de 0 a 360. Ao especificar o valor de rotação, podemos girar o carimbo em torno de seu ponto central. Se um Stamp é um objeto do tipo Stamp, então o valor de rotação pode ser especificado como aStamp.Rotation = 90. Nesse caso, o carimbo será girado a 90 graus em torno do centro do conteúdo do carimbo. O seguinte trecho de código mostra como girar o carimbo em torno do ponto central: 

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-RotatingStamp-RotatingStamp.cs" >}}