---
title: 中心点についてのスタンプの回転
type: docs
weight: 10
url: /ja/net/rotating-stamp-about-the-center-point/
description: このセクションでは、Stampクラスを使用してスタンプを中心点で回転させる方法を説明します。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) in [Aspose.PDF for .NET](/pdf/ja/net/) は、既存のPDFファイルにスタンプを追加することを可能にします。時には、ユーザーはスタンプを回転させる必要があります。この記事では、スタンプを中心点で回転させる方法を見ていきます。

{{% /alert %}}

## 実装の詳細

[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) クラスは、PDFファイルに透かしを追加することを可能にします。 You can specify image to be added as a stamp using [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/bindimage/methods/1) method. The [SetOrigin](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setorigin) method allows you to set the origin of the added stamp; this origin is the lower-left coordinates of the stamp. You can also set the size of the image using [SetImageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setimagesize) method.

Now, we see how the stamp can be rotated about the center of the stamp.

画像をスタンプとして追加するには、[BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/bindimage/methods/1) メソッドを使用して指定できます。[SetOrigin](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setorigin) メソッドを使用すると、追加されたスタンプの原点を設定できます。この原点は、スタンプの左下の座標です。また、[SetImageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setimagesize) メソッドを使用して画像のサイズを設定することもできます。

次に、スタンプの中心を軸にしてスタンプを回転させる方法を見てみましょう。 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) クラスは、Rotation というプロパティを提供します。このプロパティは、スタンプの内容を0から360の範囲で回転させるか取得します。0から360の任意の回転値を指定できます。回転値を指定することで、スタンプをその中心点を基準に回転させることができます。StampがStamp型のオブジェクトである場合、回転値はaStamp.Rotation = 90のように指定できます。この場合、スタンプはスタンプ内容の中心を基準に90度回転します。次のコードスニペットは、スタンプを中心点を基準に回転させる方法を示しています。