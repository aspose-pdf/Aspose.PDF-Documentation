---
title: Aspose.PDF for Java 9.3.1의 공용 API 변경 사항
type: docs
weight: 60
url: /java/public-api-changes-in-aspose-pdf-for-java-9-3-1/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

이 페이지는 **Aspose.PDF for Java 9.3.1**에 도입된 공용 API 변경 사항을 나열합니다. 새로운 공용 메서드와 사용되지 않는 메서드뿐만 아니라 기존 코드에 영향을 미칠 수 있는 Aspose.PDF for Java의 내부 동작 변경 사항도 설명합니다. 특히, 회귀로 간주될 수 있는 동작을 도입하고 기존 동작을 수정한 경우, 이는 매우 중요하며 여기에 문서화되어 있습니다.

{{% /alert %}}

## 다음 메서드가 내부화되었습니다:

com.aspose.pdf.DocumentInfo.setCreator(String)<p>
com.aspose.pdf.DocumentInfo.setProducer(String)<p>
com.aspose.pdf.FileParams.getEngineDict()

## 다음 사용되지 않는 상수가 내부화되었으며, 대신 정적 getter를 사용해야 합니다:

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

## 다음 필드가 추가되었습니다:

public static Rectangle com.aspose.pdf.Rectangle.getEmpty() - 빈 사각형을 반환합니다