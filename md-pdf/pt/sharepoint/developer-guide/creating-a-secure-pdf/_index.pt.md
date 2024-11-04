---

title: Criar um PDF Seguro no SharePoint

linktitle: Criando um PDF Seguro

type: docs

weight: 60

url: /sharepoint/creating-a-secure-pdf/

lastmod: "2020-12-16"

description: Usando a API PDF SharePoint, você pode produzir PDFs seguros e criptografados e especificar suas senhas no SharePoint.

---



{{% alert color="primary" %}}



Aspose.PDF para SharePoint suporta a criação de PDFs seguros. Instalar o Aspose.PDF para SharePoint adiciona uma opção de **Configurações de Segurança do PDF** nas Configurações do Site. Aqui, você pode definir a senha do usuário, a senha do proprietário e qualquer valor da lista de algoritmos para criptografar o PDF de saída. A lista de algoritmos fornece diferentes combinações de algoritmos de criptografia e tamanhos de chave. Passe o valor de sua escolha.



Este artigo demonstra como usar o Aspose.PDF para SharePoint para gerar um PDF criptografado.



{{% /alert %}}



## **Criando um PDF Seguro**



Para demonstrar o recurso, primeiro configuramos a opção de **Configuração de Segurança do PDF** para senha do proprietário e usuário e algoritmo de criptografia. O exemplo então mescla dois documentos de uma biblioteca de documentos.



### **Definindo Opções de Configuração de Segurança de PDF**



Abra a opção **Configurações de Segurança de PDF** nas Configurações do Site e defina o algoritmo, a senha do proprietário e a senha do usuário.



Especifique diferentes senhas de usuário e proprietário ao criptografar o arquivo PDF.



- A senha do usuário, se definida, é o que você precisa fornecer para abrir um PDF. O Acrobat Reader solicita que um usuário insira a senha de usuário. Se estiver errada, o documento não abre.

- A senha do proprietário, se definida, controla permissões como impressão, edição, extração, comentários, etc. O Acrobat Reader desabilita esses recursos com base nas configurações de permissão. O Acrobat requer essa senha se você quiser definir/alterar permissões.



![todo:image_alt_text](creating-a-secure-pdf_1.png)



### **Mesclar Documentos**



Mescle dois documentos usando a opção **Converter para PDF**. Este recurso mescla vários arquivos não PDF (HTML, texto ou imagem) em um arquivo PDF.



1. Abra uma biblioteca de documentos e selecione os documentos desejados da lista.

![todo:image_alt_text](creating-a-secure-pdf_2.png)

1. Use a opção **Mesclar para PDF** nas Ferramentas de Biblioteca para salvar o arquivo de saída. Você será solicitado a salvar o arquivo de saída no disco.

![todo:image_alt_text](creating-a-secure-pdf_3.png)

### **Saída**

O arquivo de saída está criptografado.

![todo:image_alt_text](creating-a-secure-pdf_4.png)