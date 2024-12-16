---
title: 이미지 배치 작업
linktitle: 이미지 배치
type: docs
weight: 50
url: /ko/java/working-with-image-placement/
description: 이 섹션에서는 Java 라이브러리를 사용하여 PDF 파일의 이미지 배치 작업 기능을 설명합니다.
lastmod: "2021-06-05"
---

Aspose.PDF for Java는 [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber), [ImagePlacementCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementCollection)이라는 클래스를 도입하여 PDF 문서에서 이미지의 해상도 및 위치를 얻는 유사한 기능을 제공합니다.

- ImagePlacementAbsorber는 ImagePlacement 객체 컬렉션으로 이미지 사용 검색을 수행합니다.
- ImagePlacement는 실제 이미지 배치 값을 반환하는 멤버 Resolution과 Rectangle을 제공합니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;


import javax.imageio.ImageIO;

public class ExampleWorkingWithImagePlacement {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void WorkingWithImagePlacement() throws IOException {
        // 소스 PDF 파일 로드
        Document doc = new Document(_dataDir + "ImageInformation.pdf");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // 첫 번째 페이지의 내용 로드
        doc.getPages().get_Item(1).accept(abs);
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // 이미지 속성 가져오기
            System.out.println("image width:" + imagePlacement.getRectangle().getWidth());
            System.out.println("image height:" + imagePlacement.getRectangle().getHeight());
            System.out.println("image LLX:" + imagePlacement.getRectangle().getLLX());
            System.out.println("image LLY:" + imagePlacement.getRectangle().getLLY());
            System.out.println("image horizontal resolution:" + imagePlacement.getResolution().getX());
            System.out.println("image vertical resolution:" + imagePlacement.getResolution().getY());

            // 보이는 치수로 이미지 가져오기
            // Bitmap scaledImage;
            // 리소스에서 이미지 가져오기
            ByteArrayOutputStream imageStream = new ByteArrayOutputStream();
            imagePlacement.getImage().save(imageStream, ImageType.getPng());

            // Bitmap resourceImage = (Bitmap)Bitmap.FromStream(imageStream);
            BufferedImage resourceImage = ImageIO.read(new ByteArrayInputStream(imageStream.toByteArray()));

            // 실제 치수로 비트맵 생성
            BufferedImage scaledImage = toBufferedImage( 
            resourceImage.getScaledInstance((int) imagePlacement.getRectangle().getWidth(),
                    (int) imagePlacement.getRectangle().getHeight(), java.awt.Image.SCALE_SMOOTH));

            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ImageIO.write(scaledImage, "jpg", baos);
            ByteArrayInputStream fis = new ByteArrayInputStream(baos.toByteArray());

            imagePlacement.getImage().replace(fis);
        }
    }
    
    public static BufferedImage toBufferedImage(java.awt.Image img) {
        if (img instanceof BufferedImage) {
            return (BufferedImage) img;
        }

        // 투명성이 있는 버퍼링된 이미지 생성
        BufferedImage bimage = new BufferedImage(img.getWidth(null), img.getHeight(null), BufferedImage.TYPE_INT_ARGB);

        // 버퍼링된 이미지에 이미지 그리기
        Graphics2D bGr = bimage.createGraphics();
        bGr.drawImage(img, 0, 0, null);
        bGr.dispose();

        // 버퍼링된 이미지 반환
        return bimage;
    }
}
```