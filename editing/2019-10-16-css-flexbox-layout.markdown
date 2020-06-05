---
layout: post
title: Css Flexbox
date:   2019-10-16 21:03:36 +0530
categories: css
---

<h4>Background</h4>

Flexbox Layout module được tạo ra nhằm mục đích cung cấp một cách hiệu quả trong việc lay out, căn chỉnh, phân phối không gian giữa các phần tử bên trong container, ngay cả khi kích thước của chúng là chưa xác định (flex).

Ý tưởng chính của Flexbox layout là cung cấp cho container khả năng thay đổi chiều cao, chiều rộng của các phần tử trong nó để lấp đầy khoảng trống một cách phù hợp nhất với hầu hết các kích thước thiết bị hiện thị. Một flex container sẽ mở rộng phần tử của nó để lấp đầy không gian trống và co phần tử để tránh bị overflow.

Một điều quan trọng, Flexbox layout là đa hướng, trái ngược với các layout thông thường (Block theo chiều dọc, Inline theo chiều ngang). 

<h4>Cơ bản và thuật ngữ</h4>

Nếu các layout thông thường dựa trên flow direction là block và inline, flex layout dựa trên "flex-direction". Hình bên dưới sẽ giải thích điều này:

![imgage](https://css-tricks.com/wp-content/uploads/2018/11/00-basic-terminology.svg)

Các item sẽ huặc được đặt theo main axis (từ main start đến main end) huặc là chiều dọc (từ cross-start đến cross-end). 

* **main axis**: Trục chính của Flex direction là trục cơ sở, nơi là các item được đặt vào. Nó không nhất thiết là trục lằm ngang, mà nó phụ thuộc vào giá trị của thuộc tính `flex-direction`.

* **main-size:** Là chiều rộng huặc chiều dài của các phần tử, bất cứ cái nào mà lằm trong trục chính thì đều là kích thước của main-size. 

* **cross-size:** Là kích thước chiều rộng huặc chiều cao của các item, bất cứ cái nào lằm bên trong kích thước của trục vuông góc với trục chính thì đều là kích thước của cross size.

![container](https://css-tricks.com/wp-content/uploads/2018/10/01-container.svg)

<h5>Thuộc tính của container</h5>

* **display:** Đây là thuộc tính định nghĩa một flexbox. 
    ```
    .container {
        display: flex; /* or inline-flex */
    }
    ```

* **flex-direction:** Thuộc tính khởi tạo trục chính của flexbox. Flexbox là một khái niệm layout đơn hướng. Các item được đặt dọc theo hàng hang huặc hàng dọc.

    ```
    .container {
        flex-direction: row | row-reverse | column | column-reverse;
    }
    ```

* **flex-wrap:**

    ![flex-wrap](https://css-tricks.com/wp-content/uploads/2018/10/flex-wrap.svg)

    Ở chế độ mặc định thì tất cả các flex item sẽ cố gắng được đặt trong một hàng. Bạn có thể thay đổi, cho phép các phần tử được bọc lại khi cần thiết.

    ```
    .container{
        flex-wrap: nowrap | wrap | wrap-reverse;
    }
    ```

    * **nowrap**: ở chế độ mặc định thì các phần tử sẽ được đặt trên một hàng.
    * **wrap:** Các flex item sẽ được bọc lại vào nhiều hàng, từ trên xuống dưới.

    * **wrap-reverse**: Các flex item sẽ được bọc lại vào nhiều hàng, và từ dưới lên trên.

    
    
    ![wrap-demo](https://i.imgur.com/AFiolNb.png)

    *Hình trên: đỏ là nowrap, vàng là wrap.*


* **flex-flow:** Nó là một thuộc tính rút gọn, kết hợp của thuộc tính ``flex-direction ``và ``flex-wrap``. 


    ```
    div {
        display: flex;
        flex-flow: row-reverse wrap;
    }
    ```

* **justify-content:** 

    ![justify-content](https://css-tricks.com/wp-content/uploads/2018/10/justify-content.svg)

    Thuộc tính định nghĩa sự căn chỉnh của các flex item theo trục chính. Nó giúp phân phối không gian trống. Chúng cũng cố găng quản lý sự căn chỉnh của các item khi mà chúng tràn ra khỏi dòng.

    ```
    .container {
        justify-content: flex-start | flex-end | 
        center |   space-between | space-around | space-evenly | start |  
         end | left | right 
        ... + safe | unsafe;
    }
    ```

* **align-items:** 

    ![align-items](https://css-tricks.com/wp-content/uploads/2018/10/align-items.svg)


    Thuộc tính này định nghĩa các mà các flex item được đặt trên trục cross-axis (trục vuông góc với trục chính). 


    ```
    .container {
          align-items: stretch | flex-start | flex-end | 
          center |       baseline | first baseline |
           last baseline | start | end    
            | self-start | self-end +
             ... safe | unsafe;
    }
    ```

* **align-content**: 

    ![img](https://css-tricks.com/wp-content/uploads/2018/10/align-content.svg)

    Thuộc tính này căn chỉnh dòng của flex container khi mà có không gian trống trên trục cross-axis. Tương tự như cách mà ``justify-content`` căn chỉnh các item trên trục chính main-axis, ở đây thay vì căn chỉnh item thì nó căn chỉnh dòng item

<h5>Thuộc tính của Items</h5>

* **order:** 
    ![order](https://css-tricks.com/wp-content/uploads/2018/10/order.svg)
Ở chế độ mặc định thì các item được xuất hiện theo thứ tự nó xuất hiện trên cây dom. Thuộc tính này quản lý thứ tự xuất hiện của item trên flex container. 

    ```
    item {
        order: <integer>; /* default is 0 */
    }
    ```

* **flex-grow:** 

    ![flex-grow](https://css-tricks.com/wp-content/uploads/2018/10/flex-grow.svg)

    Thuộc tính này định nghĩa khả năng thay đổi kích thước của một flex-item nếu cần thiết. Nó chấp nhận một giá trị dựa trên một tỉ lệ. Nó quy định khoảng không gian mà item có thể chiếm bên trong container. Nếu tất các các item được set flex-grow là 1 thì không gian sẽ được phân phối đều. 

    ```
    .item {
        flex-grow: <number>; /* default 0 */
    }
    ```

* ``flex-shrink:``  Thuộc tính quy định khả năng co lại của item nếu cần thiết. 

    ```
    .item {
    flex-shrink: <number>; /* default 1 */
    }
    ```

* **flex-basis:** Thuộc tính này định nghĩa kích thước mặc định của một phần tử trước khi không gian còn lại được phân phối.

    ```
    .item {
    flex-basis: <length> | auto; /* default auto */
    }
    ```
    Từ khóa `auto` chỉ ra rằng "hãy nhìn vào kích thước chiều rộng huặc chiều dài của tôi". Nếu được set là 0 thì kích thước xung quanh nội dung không được tính. Nếu được set auto thì không gian mở rộng sẽ được phân phối dựa trên giá trị của flex-grow.

    
* **flex**: đây là cú pháp rút gọn của ba thuốc tính: `flex-grow`, `flex-shrink` và `flex-basis`. Thuộc tính hai và ba là tùy chọn, ở chế độ mặc định giá trị sẽ là: 0 1 auto.

    Thuộc tính này được khuyến nghị sử dụng hơn là việc set từ giá trị cho từ thuộc tính đơn lẻ. 

* **align-self:** Thuộc tính này cho phép căn chỉnh một item xác định. Sự căn chỉnh cũng tương tự như `align-items`. Nó căn chỉnh item dựa vào trục cross axis.

    ```
    .item {
    align-self: auto | flex-start | flex-end | center | baseline | stretch;
    }
    ```

    ![align-self](https://css-tricks.com/wp-content/uploads/2018/10/align-self.svg)



Tham khảo: [The complete Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)