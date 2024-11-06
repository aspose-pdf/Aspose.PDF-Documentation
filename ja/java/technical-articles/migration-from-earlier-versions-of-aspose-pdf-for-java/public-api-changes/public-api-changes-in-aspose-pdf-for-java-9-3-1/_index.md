---
title: Aspose.PDF for Java 9.3.1におけるパブリックAPIの変更
type: docs
weight: 60
url: ja/java/public-api-changes-in-aspose-pdf-for-java-9-3-1/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

このページでは、**Aspose.PDF for Java 9.3.1**で導入されたパブリックAPIの変更点を一覧表示します。新しいパブリックメソッドや廃止されたパブリックメソッドだけでなく、既存のコードに影響を与える可能性のあるAspose.PDF for Javaの内部動作の変更点についても説明します。回帰と見なされ、既存の動作を変更する可能性のある動作は特に重要であり、ここに記載されています。

{{% /alert %}}

## 以下のメソッドが内部化されました:

com.aspose.pdf.DocumentInfo.setCreator(String)<p>
com.aspose.pdf.DocumentInfo.setProducer(String)<p>
com.aspose.pdf.FileParams.getEngineDict()

## 以下の非推奨の定数が内部化され、代わりに静的ゲッターを使用する必要があります:

com.aspose.pdf.ImageFormatInternal.Bmp<p>
com.aspose.pdf.ImageFormatInternal.Emf<p>

com.aspose.pdf.ImageFormatInternal.Exif<p>
com.aspose.pdf.ImageFormatInternal.Gif<p>  
com.aspose.pdf.ImageFormatInternal.Jpeg<p>  
com.aspose.pdf.ImageFormatInternal.Icon<p>  
com.aspose.pdf.ImageFormatInternal.MemoryBmp<p>  
com.aspose.pdf.ImageFormatInternal.Png<p>  
com.aspose.pdf.ImageFormatInternal.Tiff<p>  
com.aspose.pdf.ImageFormatInternal.Wmf<p>  
com.aspose.pdf.TextEncodingInternal.ASCII<p>  
com.aspose.pdf.TextEncodingInternal.BigEndianUnicode<p>  
com.aspose.pdf.TextEncodingInternal.Default<p>  
com.aspose.pdf.TextEncodingInternal.Unicode<p>  
com.aspose.pdf.TextEncodingInternal.UTF32<p>  
com.aspose.pdf.TextEncodingInternal.UTF32BE<p>  
com.aspose.pdf.TextEncodingInternal.UTF7<p>  
com.aspose.pdf.TextEncodingInternal.UTF8<p>  
com.aspose.pdf.TextEncodingInternal.UTF8Unmarked  

## 以下のフィールドが追加されました:

public static Rectangle com.aspose.pdf.Rectangle.getEmpty() - 空の長方形を返します