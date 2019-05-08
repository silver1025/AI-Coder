package main.java;

import com.intellij.codeInsight.completion.*;
import com.intellij.codeInsight.lookup.LookupElement;
import com.intellij.codeInsight.lookup.LookupElementBuilder;
import com.intellij.openapi.editor.Document;
import com.intellij.openapi.editor.Editor;
import com.intellij.patterns.PlatformPatterns;
import com.intellij.patterns.PsiElementPattern;
import com.intellij.psi.PsiPlainText;
import com.intellij.util.ProcessingContext;
import org.jetbrains.annotations.NotNull;

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import net.sf.json.JSONArray;
import net.sf.json.JSONObject;
import org.jetbrains.annotations.Nullable;
// MyCompletionContributor.java

public class MyCompletionContributor extends CompletionContributor {

    /*public MyCompletionContributor() {
        //super();
        System.out.println("in the constructor");
        extend(CompletionType.BASIC,
                PlatformPatterns.psiElement(PsiPlainText.class),
                //PlatformPatterns.psiElement(Psi),
                new CompletionProvider<CompletionParameters>() {
                    public void addCompletions(@NotNull CompletionParameters parameters,
                                               ProcessingContext context,
                                               @NotNull CompletionResultSet resultSet) {
                        Document document = parameters.getEditor().getDocument();
                        String str = document.getText();
                        System.out.println(str + "in the constructor");
                        resultSet.addElement(LookupElementBuilder.create("Hello"));
                    }
                }
        );
        *//*PsiElementPattern pattern = PlatformPatterns
                .psiElement(JSElementTypes.REFERENCE_EXPRESSION);
        MyCompletionProvider completionProvider = new MyCompletionProvider();
        extend(CompletionType.BASIC, pattern, completionProvider);*//*
    }*/

    @Nullable
    @Override
    public String handleEmptyLookup(@NotNull CompletionParameters parameters, Editor editor) {
        System.out.println("in here empty completion");
        //result.addElement(LookupElementBuilder.create(li));
        return "sorry no suggestions";
        //return super.handleEmptyLookup(parameters, editor);
    }

    @Override
    public void fillCompletionVariants(@NotNull CompletionParameters parameters, @NotNull CompletionResultSet result) {
        //System.out.println("in here fill completion");
        //System.out.println(parameters.toString());
        Document document = parameters.getEditor().getDocument();
        String str = document.getText();
        //测试，简单添加三个推荐字符串，且带上不同的优先级，值越大优先级越高
        result.addElement(
                PrioritizedLookupElement.withPriority(
                        LookupElementBuilder
                                .create("hello2"),
                        1003
                )
        );
        result.addElement(
                PrioritizedLookupElement.withPriority(
                        LookupElementBuilder
                                .create("hello1"),
                        1002
                )
        );
        result.addElement(
                PrioritizedLookupElement.withPriority(
                        LookupElementBuilder
                                .create("hello3"),
                        1001
                )
        );
        //下面的是实际使用模型来返回推荐结果的代码
        /*try {
            String strs[] = str.split("\n");
            String key = strs[strs.length-1];
            key = key.trim();
            key = key.replaceAll(" ", "%20");
            //key = URLEncoder.encode(key);
            //System.out.println(key);
            //System.out.println(str);
            //请求的webservice的url
            String urlStr = "http://127.0.0.1:9078/plugin_test?keyword="+key;
            //String query = "hello";
            //JSONArray
            JSONObject jsonObject = null;
            URL url = new URL(urlStr);
            //创建http链接
            HttpURLConnection httpURLConnection = (HttpURLConnection) url.openConnection();
            //设置请求的方法类型
            httpURLConnection.setRequestMethod("GET");
            //设置请求的内容类型
            httpURLConnection.setRequestProperty("Content-type", "application/x-www-form-urlencoded");
            //设置发送数据
            httpURLConnection.setDoOutput(true);
            //设置接受数据
            httpURLConnection.setDoInput(true);
            //发送数据,使用输出流
            //OutputStream outputStream;
            //outputStream = httpURLConnection.getOutputStream();//发送的soap协议的数据
            //String requestXmlString = requestXml("北京");
            //String content = "keyword="+ URLEncoder.encode(query, "utf-8");
            //发送数据
            //outputStream.write(content.getBytes());
            //接收数据
            InputStream inputStream = httpURLConnection.getInputStream();
            //定义字节数组
            byte[] b = new byte[1024];
            //定义一个输出流存储接收到的数据
            ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
            //开始接收数据
            int len = 0;
            while (true) {
                len = inputStream.read(b);
                if (len == -1) {
                    //数据读完
                    break;
                }
                byteArrayOutputStream.write(b, 0, len);
            }
            //从输出流中获取读取到数据(服务端返回的)
            String response = byteArrayOutputStream.toString();
            //System.out.println("response:"+response);
            jsonObject = JSONObject.fromObject(response);
            String listStr = jsonObject.get("data").toString();
            listStr = listStr.substring(1,listStr.length()-1).replace("\"", "");
            //System.out.println(listStr);
            String[] lists = listStr.split(",");
            //CompletionResultSet completionResultSet = result.withPrefixMatcher();
            for(String li: lists){
                LookupElement r = LookupElementBuilder.create(li);
                //r.
                result.addElement(r);
                //System.out.println(li);
            }
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }*/
        super.fillCompletionVariants(parameters, result);
    }
}
