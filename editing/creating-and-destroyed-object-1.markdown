---
layout: post
title: Consider static factory methods instead of constructors
date: 2019-09-27 11:01:03 +0530
categories: Java
---

<h4>Item1: Xem xét thay thế constructor bằng static factory method</h4>

Cách truyền thống để một class cho phép một client lấy một thực thể là cung cấp một constructor. Có một kỹ thuật khác mà nó nên trở thành một phần của bộ công cụ của mọi lập trình viên. Một class có thể cung cấp một `static factory method`, nó đơn giản là một phương thức static trả về một thực thể của class. Dưới đây là một ví dụ đơn giản về việc chuyển biến boolean cơ bản sang Boolean object tham chiếu.

```
public static Boolean valueOf(boolean b){
    return b ? Boolean.TRUE : Boolean.FALSE;
}
```

Chú ý rằng `static factory method` không tương đương với `Factory Method` trong Design patternt. 

<h5>Lợi ích</h5>

<h6>1. Không giống với constructor, static factory method có tên.</h6>

Ví dụ khi chúng ta muốn tạo một số lớn: 
```
public BigInteger(int, int, Random)
```

Chúng return một BigInteger, có thể  số integer đó là một số nguyên tốt. Thay vì sử dụng constructor gây khó hiểu như trên thì ta có thể dùng `static factory method`:

```
public static BigInteger probablePrime(){

}
```

Lập trình viên có thể xử lý các giới hạn này bằng việc thêm vào các constructor với danh sách tham số khác nhau, tuy nhiên đây là một cách rất tệ. Những người dùng nó, như là API  sẽ có thể nhầm lẫn và sử dụng sai constructor. Khi sử dung `static fatory method` chúng ta sẽ không gặp phải những giới hạn kể trên.

<h6>2. Lợi ích thứ hai là không giống như constructor, static factory method không yêu cầu tạo mới một object khi được gọi.</h6>

Nó cho phép chúng ta tạo ra các class không thể thay đổi, mà ta sử dụng các thực thể được cấu trúc sẵn. Huặc là sử dụng để cache các thực thể mà chúng ta đã tạo, nhằm tránh tạo ra các lặp thực thể không cần thiết. 

Khả năng của `static factory method` cho phép trả về cùng một thực thể từ những lần gọi khác nhau, cho phép lớp duy trì nghiêm ngặt các kiểm soát lên thực thể, tại mọi thời điểm.

<h6>3. Không giống như constructor, lợi ích thứ ba mà static factory method mang lại là nó có thể trả về một đối tượng của bất kỳ kiểu con nào của kiểu trả về của nó.</h6>

Nó cho ta một khả năng linh họat trong việc chọn lớp của object được trả về.

Một ứng dụng của sự linh hoạt này là một API có thể trả về một đối tượng mà không cần phải pulibc class của chúng ta. Ẩn implement của các class trong cách làm này cho chúng ta muộn API vô cùng gọn nhẹ. 