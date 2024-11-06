---
title: Aspose.PDF for Java 9.3.0 のパブリック API 変更
type: docs
weight: 50
url: ja/java/public-api-changes-in-aspose-pdf-for-java-9-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

このページでは、[Aspose.PDF for Java 9.3.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry559320.aspx) で導入されたパブリック API の変更点を一覧にしています。新たに追加されたパブリックメソッドや廃止されたパブリックメソッドだけでなく、既存のコードに影響を与える可能性のある Aspose.PDF for Java の裏での動作の変更についても説明しています。既存の動作を変更する可能性があるリグレッションとして見なされる動作は特に重要であり、ここに記録されています。

{{% /alert %}}

## 追加されたクラス:

com.aspose.pdf.MemoryCleaner
com.aspose.pdf.generator.legacy.CmykColorSpace
com.aspose.pdf.generator.legacy.GrayColorSpace
com.aspose.pdf.generator.legacyxmlmodel.ClippingPath
com.aspose.pdf.generator.legacyxmlmodel.ColouredTilingPattern

com.aspose.pdf.generator.legacyxmlmodel.CompareValidator
com.aspose.pdf.generator.legacyxmlmodel.クロスハッチパターン  
com.aspose.pdf.generator.legacyxmlmodel.カスタムバリデーター  
com.aspose.pdf.generator.legacyxmlmodel.関数  
com.aspose.pdf.generator.legacyxmlmodel.関数指数補間  
com.aspose.pdf.generator.legacyxmlmodel.軸方向シェーディンググラデーション  
com.aspose.pdf.generator.legacyxmlmodel.放射状シェーディンググラデーション  
com.aspose.pdf.generator.legacyxmlmodel.ハッチングパターン  
com.aspose.pdf.generator.legacyxmlmodel.イメージパターン  
com.aspose.pdf.generator.legacyxmlmodel.ポイントパターン  
com.aspose.pdf.generator.legacyxmlmodel.範囲バリデーター  
com.aspose.pdf.generator.legacyxmlmodel.正規表現バリデーター  
com.aspose.pdf.generator.legacyxmlmodel.必須フィールドバリデーター  
com.aspose.pdf.generator.legacyxmlmodel.シェーディンググラデーションパターン  
com.aspose.pdf.generator.legacyxmlmodel.シェーディングパターン  
com.aspose.pdf.generator.legacyxmlmodel.シェーディングパターンファクトリー  
com.aspose.pdf.generator.legacyxmlmodel.タイルパターン  
com.aspose.pdf.generator.legacyxmlmodel.無色タイルパターン  

com.aspose.pdf.Artifact.アーティファクトタイプ
com.aspose.pdf.Artifact.ArtifactSubtype  
com.aspose.pdf.ILicenseProvider  
com.aspose.pdf.Layer  
com.aspose.pdf.LettersPositioningMethods  

## 列挙クラスが追加されました:

com.aspose.pdf.generator.legacyxmlmodel.enums.FunctionType  
com.aspose.pdf.generator.legacyxmlmodel.enums.PaintType  
com.aspose.pdf.generator.legacyxmlmodel.enums.PatternType  
com.aspose.pdf.generator.legacyxmlmodel.enums.ShadingGradientType  
com.aspose.pdf.generator.legacyxmlmodel.enums.TilingType  
列挙クラスの使用を実装しました: **TextEncodingInternal** と **ImageFormatInternal**

## クラスが削除されました:

廃止された com.aspose.pdf.generator.legacyxmlmodel.enums.TextAlignmentType クラスは削除されました。

## クラスが移動されました:

パッケージ **com.aspose.pdf.generator.legacyxmlmodel.enums** のクラスはパッケージ **com.aspose.pdf.generator.legacyxmlmodel** に移動されました。

## クラスが内部化されました:

com.aspose.pdf.XfdfTags  
com.aspose.pdf.generator.legacyxmlmodel.NonClosedShape  
com.aspose.pdf.generator.legacyxmlmodel.ComplexShape  

com.aspose.pdf.generator.legacyxmlmodel.Circle  
com.aspose.pdf.generator.legacyxmlmodel.Curve  
com.aspose.pdf.generator.legacyxmlmodel.NonClosedShape  
com.aspose.pdf.generator.legacyxmlmodel.Ellipse  
com.aspose.pdf.generator.legacyxmlmodel.PolyDashArray  
com.aspose.pdf.generator.legacyxmlmodel.PathArea  
com.aspose.pdf.generator.legacyxmlmodel.Rectangle  

## クラスの変更:

**PdfExtractor** クラスにメソッドが追加されました  
public extractText(java.nio.charset.Charset value)  

**PdfFileEditor** クラスにメソッドが追加されました  
public static void validateAnotations(IDocument doc)  

**BorderInfo** クラスに新しいコンストラクタが追加されました:  
public BorderInfo(int borderSide)  
public BorderInfo(int borderSide, GraphInfo borderFormat)  
public BorderInfo(int borderSide, float borderWidth)  
public BorderInfo(int borderSide, float borderWidth, Color borderColor)  
public BorderInfo(int borderSide, Color borderColor)  

**Canvas** クラスにメソッドが追加されました  
public Object deepClone()  

**Cell** クラスにメソッドが追加されました:  
public boolean isNoBorder()  
public void setNoBorder(boolean value)  

public Object completeClone()  

In **DocumentAttachment** クラスにメソッドが追加されました  
public Object completeClone()

In **FloatingBox** クラスにメソッドが追加されました  
public Object completeClone()

In **FormField** クラスにメソッドが追加されました  
public Object completeClone()

In **Graph** クラスにメソッドが追加されました:  
public float getRotatingAngle()  
public void setRotatingAngle(float value)  
public ClippingPath getClipping()  
public void setClipping(ClippingPath value)  
public Object completeClone()

In **Image** クラスにコンストラクタとメソッドが追加されました:  
public Image()  
public Image(Section section)  
public int getAutoNumber()  
public void setAutoNumber(int value)  
public float getImageHeight()  
public void setImageHeight(float value)  
public float getImageWidth()  
public void setImageWidth(float value)  
public float getVectorGraphicsRenderingDPI()  
public void setVectorGraphicsRenderingDPI(float value)  
public float getImageScale()  
public void setImageScale(float value)  
public Object completeClone()  

In **ImageInfo** クラスにフィールドとメソッドが追加されました:

public TextInfo TextInfo

public String Title
public BorderInfo 画像枠

public /**ImageFileType**/int _画像ファイルタイプ
public InputStream getImageStream()
public void setImageStream(InputStream 値)
public BufferedImage getSystemImage()
public void setSystemImage(BufferedImage 値)
public /**Byte**/byte[] getMemoryData()
public void setMemoryData(/**Byte**/byte[] 値)
public boolean isFixImgWidthSettedInXML()
public void setFixImgWidthSettedInXML(boolean 値)
public boolean isFixImgHeightSettedInXML()
public void setFixImgHeightSettedInXML(boolean 値)
public boolean isAllFramesInNewPage()
public void setAllFramesInNewPage(boolean 値)
public boolean isStencilMask()
public void setStencilMask(boolean 値)
public com.aspose.pdf.generator.legacyxmlmodel.Color getBackgroundColor()
public void setBackgroundColor(com.aspose.pdf.generator.legacyxmlmodel.Color 値)
public java.awt.Color getPatternColor()
public void setPatternColor(java.awt.Color 値)

**Paragraph** クラスに追加されたフィールドとメソッド:
public float 固定高さ;

public float 固定幅;
public /**BookmarkIncludeType**/int getBookmarked()  
public void setBookmarked(/**BookmarkIncludeType**/int value)  
public void copyTo(Paragraph par)

**RadioButton** クラスにメソッドが追加されました  
public Object completeClone()

**Row** クラスにメソッドが追加されました  
public Object completeClone()

**Segment** クラスにメソッドが追加されました  
public Object completeClone()

**Shape** クラスにメソッドが追加されました  
public float getOpacity()  
public void setOpacity(float value)  
public float getStrokeOpacity()  
public void setStrokeOpacity(float value)  

**Shapes** クラスでは一部のメソッドが内部化されました:  
void add(Shape shape)  
void remove(Shape shapeToRemove)  
void copyTo(Shape[] shapeArray, int index)  
int indexOf(Shape shape)

**Table** クラスにメソッドが追加されました  
public /**override**/ Object completeClone()

**Text** クラスにメソッドが追加されました  
public /**override**/ Object completeClone()

**XslFoLoadOptions** クラスにメソッドが追加されました  
public String getBasePath()  
public void setBasePath(String value)

**PdfBookmarkEditor** クラスにメソッドが追加されました

public Bookmarks extractBookmarks(boolean upperLevel)

In **XslFoLoadOptions** クラスにメソッドが追加されました

In **XslFoLoadOptions** クラスにメソッドが追加されました

In **XslFoLoadOptions** クラスにメソッドが追加されました

In **XslFoLoadOptions** クラスにメソッドが追加されました

**isから始まっていたすべてのブール型セッターメソッド名がsetに変更されました**

例えば:

com.aspose.pdf.facades.ReplaceTextStrategy.isRegularExpressionUsed(boolean value) -> com.aspose.pdf.facades.ReplaceTextStrategy.setRegularExpressionUsed(boolean value)