$(function () {
  $(".products-owl .owl-carousel").owlCarousel({
    items: 6,
  });
    // const products = [
    //     {
    //       id: 1,
    //       name: "Mini 3D Glass",
    //       originalPrice: "0",
    //       price: "220.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/40-125x125.png",
    //       category: ["0n-sell", "hot-sell", "best-sell", "hot-arrival","Trend-arrival"],
    //     },
    //     {
    //       id: 2,
    //       name: "Kotion Headset",
    //       originalPrice: "0",
    //       price: "29.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/49-125x125.png",
    //       category: ["0n-sell", "best-sell", "hot-arrival"],
    //     },
    //     {
    //       id: 3,
    //       name: "Core i7 Laptop",
    //       originalPrice: "0",
    //       price: "125.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/04/01-125x125.png",
    //       category: ["0n-sell", "best-sell","hot-arrival"],
    //     },
    //     {
    //       id: 4,
    //       name: "Bluetooth Gamepad",
    //       originalPrice: "0",
    //       price: "199.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/45-125x125.png",
    //       category: ["0n-sell", "best-sell", "hot-arrival"],
    //     },
    //     {
    //       id: 5,
    //       name: "Waterproof Camera",
    //       originalPrice: "560.00",
    //       price: "520.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/06-125x125.png",
    //       category: ["0n-sell", "Trend"," best-sell", "on-arrival", "hot-arrival","best-arrival"],
    //     },
    //     {
    //       id: 6,
    //       name: "Stereo Headset",
    //       originalPrice: "0",
    //       price: "16.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/04/Bluetooth-Headphones-Wireless-Stereo-Headset-125x125.jpg",
    //       category: ["0n-sell", "hot-sell", "best-sell", "hot-arrival"],
    //     },
    //     {
    //       id: 7,
    //       name: "Apple iPhone 6s",
    //       originalPrice: "0",
    //       price: "299.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/21-125x125.png",
    //       category: ["0n-sell", "best-sell", "hot-arrival"],
    //     },
    //     {
    //       id: 8,
    //       name: "Moving Camera",
    //       originalPrice: "0",
    //       price: "230.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/07-125x125.png",
    //       category: ["0n-sell", "best-sell", "hot-arrival"],
    //     },
    //     {
    //       id: 9,
    //       name: "Golden Bluetooth",
    //       originalPrice: "23.00",
    //       price: "12.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/04/Headphones-Wireless-Stereo-Headsets-earbuds-with-Mic-125x125.jpg",
    //       category: ["0n-sell", "Trend", "best-sell", "hot-arrival"],
    //     },
    //     {
    //       id: 10,
    //       name: "Waterproof Camera",
    //       originalPrice: "720.00",
    //       price: "540.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/04/camera-drone-125x125.png",
    //       category: ["0n-sell", "furniture"],
    //     },  
    //     {
    //       id: 11,
    //       name: "Bluetooth Speaker",
    //       originalPrice: "0",
    //       price: "70.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2013/06/HTB1olbtmlDH8KJj-125x125.jpg",
    //       category: ["0n-sell", "best-sell"],
    //     },
    //     {
    //       id: 12,
    //       name: "Xpeed Headset",
    //       originalPrice: "600.00",
    //       price: "560.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2013/06/DEEP-BASS-Headphones-Earphones-3-5mm-AUX-Foldable-Portable-Adjustable-Gaming-Headset-For-Phones-MP3-MP4-125x125.jpg",
    //       category: ["0n-sell", "hot-sell","best-sell", "Trend-arrival"],
    //     },
    //     {
    //       id: 13,
    //       name: "Mic for Phone",
    //       originalPrice: "0",
    //       price: "70.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/Speaker-Cannon-2-Mini-Smart-Bluetooth-125x125.png",
    //       category: ["0n-sell", "best-sell","hot-arrival"],
    //     },
    //     {
    //       id: 14,
    //       name: "Sony Gamepad",
    //       originalPrice: "0",
    //       price: "110.00-$120.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2013/06/Gamepad-for-Sony-Playstation-3-125x125.jpg",
    //       category: ["0n-sell", "best-sell"],
    //     },
    //     {
    //       id: 15,
    //       name: "3D Glass",
    //       originalPrice: "640.00",
    //       price: "540.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2013/06/3D-VR-Glass-Virtual-Reality-125x125.jpg",
    //       category: ["0n-sell", "best-sell", "Trend-arrival"],
    //     },   
    //     {
    //       id: 16,
    //       name: "wireless Speaker",
    //       originalPrice: "0",
    //       price: "65.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/04/REMAX-Portable-Wireless-Bluetooth-Speaker-125x125.jpg",
    //       category: ["0n-sell", "best-sell", "hot-arrival"],
    //     },
    //     {
    //       id: 17,
    //       name: "Drone WI FI FPV",
    //       originalPrice: "280.00",
    //       price: "250.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2013/06/Drone-jjrc-X3-hax-WI-FI-FPV-1-125x125.jpg",
    //       category: ["0n-sell", "best-sell","Trend-arrival"],
    //     },
    //     {
    //       id: 18,
    //       name: "Gaming Headphones",
    //       originalPrice: "69.00",
    //       price: "42.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2013/06/DEEP-BASS-Headphones-Earphones-3-5mm-AUX-Foldable-Portable-Adjustable-Gaming-Headset-For-Phones-MP3-MP4-2-125x125.jpg",
    //       category: ["0n-sell", "best-sell"],
    //     },
    //     {
    //       id: 19,
    //       name: "Xpeed Laptop",
    //       originalPrice: "640.00",
    //       price: "540.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/04/laptop_features_1-125x125.jpg",
    //       category: ["hot-sell", "on-arrival", "Trend-arrival", "best-arrival"],
    //     },   
    //     {
    //       id: 20,
    //       name: "Xpeed Laptop V2",
    //       originalPrice: "0",
    //       price: "699.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/laptop_features_21-125x125.jpg",
    //       category: ["hot-sell", "Trend-arrival"],
    //     },  
    //     {
    //       id: 21,
    //       name: "Black Solid Color Full Sleeve",
    //       originalPrice: "0",
    //       price: "29.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/30-125x125.png",
    //       category: ["hot-sell", "Trend-arrival"],
    //     },
    //     {
    //       id: 22,
    //       name: "Smart TV",
    //       originalPrice: "0",
    //       price: "30.00-$280.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2013/06/LED-32-LG-32LJ500U-1-125x125.jpg",
    //       category: ["hot-sell", "hot-sell", "Trend-arrival"],
    //     },
    //     {
    //       id: 23,
    //       name: "3D VR Glass",
    //       originalPrice: "0",
    //       price: "245.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2013/06/3D-VR-Glass-125x125.jpg",
    //       category: ["hot-sell", "Trend-arrival" ],
    //     },
    //     {
    //       id: 24,
    //       name: "Zhndu Mobile",
    //       originalPrice: "230.00",
    //       price: "160.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2013/06/Zhndu-Mobile-1-125x125.png",
    //       category: ["hot-sell", "Trend-arrival"],
    //     },
    //     {
    //       id: 25,
    //       name: "Xpeed Mobile",
    //       originalPrice: "230.00",
    //       price: "160.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2013/06/Zhndu-Mobile-1-125x125.png",
    //       category: ["hot-sell", "on-arrival", "Trend-arrival","best-arrival"],
    //     },   
    //     {
    //       id: 26,
    //       name: "Touchscreen Laptop",
    //       originalPrice: "640.00",
    //       price: "540.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2013/06/13-3-VBOOK-V3-Tablet-PC-with-Fingerprint-Recognition-IPS-Touchscreen-Core-i7-6500U-laptop-2-125x125.jpg",
    //       category: ["hot-sell", "furniture"],
    //     },
    //     {
    //       id: 27,
    //       name: "Mens Watches",
    //       originalPrice: "0",
    //       price: "240.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2013/06/Mens-Watches-125x125.jpg",
    //       category: ["hot-sell", "furniture"],
    //     },
    //     {
    //       id: 28,
    //       name: "Apple iPhone 7s",
    //       originalPrice: "690.00",
    //       price: "660.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/24-125x125.png",
    //       category: ["hot-sell", "Trend", "on-arrival", "Trend-arrival", "best-arrival"],
    //     },
    //     {
    //       id: 29,
    //       name: "Professional Drone",
    //       originalPrice: "680.00",
    //       price: "660.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/18-125x125.png",
    //       category: ["hot-sell", "Trend", "on-arrival", "best-arrival"],
    //     },   
    //     {
    //       id: 30,
    //       name: "Red Strawberry",
    //       originalPrice: "0",
    //       price: "12.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/10-125x125.png",
    //       category: ["hot-sell", "furniture"],
    //     },    
    //     {
    //       id: 31,
    //       name: "JBL Evol Type DC Wifi Speaker",
    //       originalPrice: "0",
    //       price: "29.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/33-125x125.png",
    //       category: ["hot-sell", "furniture"],
    //     },
    //     {
    //       id: 32,
    //       name: "7th Generation",
    //       originalPrice: "560.00",
    //       price: "520.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/13-125x125.png",
    //       category: ["Trend", "on-arrival","best-arrival"],
    //     },
    //     {
    //       id: 33,
    //       name: "Camera Drone",
    //       originalPrice: "460.00",
    //       price: "340.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/04/gaming_console-125x125.png",
    //       category: ["Trend", "hot-arrival"],
    //     },
    //     {
    //       id: 34,
    //       name: "Camera Drone",
    //       originalPrice: "720.00",
    //       price: "540.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/04/camera-drone-125x125.png",
    //       category: ["Trend", "best-sell"],
    //     },
    //     {
    //       id: 35,
    //       name: "Game Controller",
    //       originalPrice: "60.00",
    //       price: "40.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/04/game_controller_31-125x125.png",
    //       category: ["Trend", "on-arrival","best-arrival"],
    //     },  
    //     {
    //       id: 36,
    //       name: "Mental Body Mobile",
    //       originalPrice: "720.00",
    //       price: "540.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/22-125x125.png",
    //       category: ["Trend", "furniture"],
    //     },
    //     {
    //       id: 37,
    //       name: "Holy Stone Drone",
    //       originalPrice: "560.00",
    //       price: "520.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/04/WIFI-FPV-With-720P-Camera-High-Hold-Foldable-Drones-125x125.jpg",
    //       category: ["Trend"],
    //     },
    //     {
    //       id: 38,
    //       name: "Google Glass",
    //       originalPrice: "360.00",
    //       price: "240.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/04/game_controller_21-125x125.png",
    //       category: ["Trend", "on-arrival","best-arrival"],
    //     },
    //     {
    //       id: 39,
    //       name: "Drones Helicopter",
    //       originalPrice: "720.00",
    //       price: "540.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/04/Arasdm-APP-RC-Drones-125x125.jpg",
    //       category: ["Trend", "furniture"],
    //     },
    //     {
    //       id: 40,
    //       name: "Remote Drone",
    //       originalPrice: "680.00",
    //       price: "660.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/19-125x125.png",
    //       category: ["Trend", "on-arrival","best-arrival"],
    //     }, 
    //     {
    //       id: 41,
    //       name: "Fuers Outdoor",
    //       originalPrice: "520.00",
    //       price: "499.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/05-125x125.png",
    //       category: ["Trend", "on-arrival", "best-arrival"],
    //     },
    //     {
    //       id: 42,
    //       name: "CC Camera",
    //       originalPrice: "240.00",
    //       price: "210.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/08-125x125.png",
    //       category: ["Trend", "on-arrival","best-arrival"],
    //     },
    //     {
    //       id: 43,
    //       name: "Xpeed Projector",
    //       originalPrice: "520.00",
    //       price: "499.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/05/36-158x158.png",
    //       category: ["on-arrival", "best-arrival"],
    //     },
    //     {
    //       id: 39,
    //       name: "Drones Helicopter",
    //       originalPrice: "720.00",
    //       price: "540.00",
    //       image:"https://demo.xpeedstudio.com/marketo/home3/wp-content/uploads/sites/3/2018/04/Arasdm-APP-RC-Drones-125x125.jpg",
    //       category: ["Trend", "furniture"],
    //     },                                               
    // ]
    // if(val == 0) {
    //   $("").addClass("display-none");
    // }

  // renderOwl(products,".products-owl .owl-carousel" )
  // kiem tra thang nao dang active
  const allCategory = $(".products-hot-new .category li");
  for (let i = 0; i < allCategory.length; i++) {
    if ($(allCategory[i]).hasClass("active")) {
      const category = $(allCategory[i]).data("category");
      const activeProducts = products.filter((val) =>
        val.category.includes(category)
      );
      renderOwl(activeProducts, ".products-owl .owl-carousel");
    }
  }

  $(".products-hot-new .category li").click(function (e) { 
    e.preventDefault(); // loai bo su kien mac dinh
    $(".products-hot-new .category li").removeClass("active");
    $(this).addClass("active");
    
    // lay category
    const category = $(this).data("category");

    const filterProducts = products.filter((val) =>
      val.category.includes(category)
    );

    removeOwl(products);
    renderOwl(filterProducts, ".products-owl .owl-carousel");
  });
});

function removeOwl(products) {
  for (let i = 0; i < products.length; i++) {
    $(".products-owl .owl-carousel")
      .trigger("remove.owl.carousel", [i])
      .trigger("refresh.owl.carousel");
  }
}


function renderOwl(list, selector){
   // load san pham ra owl carousel
   list.reverse().map((val, index)=> {
    $(selector)
    .trigger("add.owl.carousel", 
    [`
    <div class="xs-product-category a-center">
            <a href=""><img src="${val.image}" alt=""></a>
            <h4 class="product-title">${val.name}</h4>
            <span class="price ">
              <del><span >$${val.originalPrice}</span></del>
              <ins><span>$${val.price}</span></ins>
            </span>      
          </div>
    
    `,
    index,
  ])
    .trigger("refresh.owl.carousel")
  })
}