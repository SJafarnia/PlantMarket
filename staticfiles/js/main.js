
    $(".form-group :input").tooltip({

        // place tooltip on the right edge
        position: "center",
  
        // a little tweaking of the position
        // offset: [-2, 10],
  
        // use the built-in fadeIn/fadeOut effect
        effect: "fade",
  
        // custom opacity setting
        // opacity: 0.7
  
    });

let soilStat = "False";
let potStat = "False";


// var headertext = [];
// var headers = document.querySelectorAll("thead");
// var tablebody = document.querySelectorAll("tbody");

// for (var i = 0; i < headers.length; i++) {
// headertext[i]=[];
// for (var j = 0, headrow; headrow = headers[i].rows[0].cells[j]; j++) {
//  var current = headrow;
//  headertext[i].push(current.textContent);
//  }
// }


// for (var h = 0, tbody; tbody = tablebody[h]; h++) {
// for (var i = 0, row; row = tbody.rows[i]; i++) {
// for (var j = 0, col; col = row.cells[j]; j++) {
//    col.setAttribute("data-th", headertext[h][j]);
//   }

// }}

function xdd(){
    $('html,body').animate({
        scrollTop: $("#ft").offset().top},
        'slow');
}

function showFactor(){
      $.get('http://127.0.0.1:8000/auth/factor/'
    ).then(res=>{
        $(".ajx-div").html(res);
        $('html,body').animate({
        scrollTop: $(".ajx-div").offset().top},
        'slow');
    });
}

function showFactorDetails(){
      $.get('http://127.0.0.1:8000/auth/factor/detail'
    ).then(res=>{
        $(".ajx-div").html(res)
    });
      $('html,body').animate({
        scrollTop: $(".ajx-div").offset().top},
        'slow');
}

function addAddress() {
    $.get('http://127.0.0.1:8000/auth/credential/add-a'
    ).then(res => {
        $(".ajx-div").html(res)
    })
}

function addAddress2() {
    $.get('http://127.0.0.1:8000/orders/card/address/n/'
    ).then(res => {
        $(".calit").html(res)
    })
}


function addAddr(){
    let bt = document.getElementById("sve");
    let url = 'http://127.0.0.1:8000/auth/credential/add-a/';
        let form = $('.a-u-a-f')
        let csrf = $("input[name=csrfmiddlewaretoken]").val();
        
        form.submit((e)=>{    
            e.preventDefault();

            let fd = new FormData(form[0]);
    
            function handleEdit(oldRes){
                $(".ajx-div").html(oldRes);
                // let form = $(".a-u-a-f");
                
                // let csrf = $("input[name=csrfmiddlewaretoken]").val();
                
                form.submit((e)=>{    
                    e.preventDefault();    
                    let fd = new FormData(form[0])
                    $.ajax({
                        type: "POST",
                        url: url,
                        data: fd,
                        headers: {
                            "X-CSRFToken": csrf
                        },
                        success: (res) => {
                                            
                                if (res["fv"]== "formvalidated"){
                                    
                                    showAddresses()
                                    
                            } else {
                                handleEdit(oldRes);
                            }
                        },

                        error: (err) => {
                            console.log(err)
                        },
                        processData: false,
                        contentType: false,
                        crossDomain: true,
                        // cache:false,
                        // processData: false
                    })
            })
        }
            $.ajax({
            type: "POST",
            url: url,
            data: fd,
            headers: {
                "X-CSRFToken": csrf
            },
            success: (res) => {
                if (res["fv"]== "formvalidated"){
                    // console.log(res["fv"])
                    showAddresses()
                    
       
                }else{
                    console.log("hgc")
                    handleEdit(res)
                }
            },

            error: (err) => {
                console.log(err)
            },
            processData: false,
            contentType: false,
            crossDomain: true,
            // cache:false,
            // processData: false
        })
    })

}

function editAddress(id) {
    let url = 'http://127.0.0.1:8000/auth/credential/edit-a/'+id
    $.get(url
    ).then(res => {
        $(".ajx-div").html(res)
            let form = $('.a-u-a-f')
            let csrf = $("input[name=csrfmiddlewaretoken]").val();
            // let addr = $("#id_address");
            // let postC = $("#id_postal_code");
            // let block = $("#id_block");
            // let N = $("#id_N");
            // let id = $("#id_id");
        // console.log("kir2");
        // form.on("submit", (event)=>{
        form.submit((e)=>{    
            e.preventDefault();

            let fd = new FormData(form[0]);
            // console.log(fd)
            function handleEdit(oldRes){
            $(".ajx-div").html(oldRes);
            // let form = $(".a-u-a-f");
            // let form = document.getElementsByClassName("a-u-a-f")[0]
            
                // console.log(form);
            // let csrf = $("input[name=csrfmiddlewaretoken]").val();
                // console.log(csrf);
            // form.on("submit", (event)=> {
                form.submit((e)=>{
                e.preventDefault();
                let fd = new FormData(form[0])
                $.ajax({
                    type: "POST",
                    url: url,
                    data: fd,
                    headers: {
                        "X-CSRFToken": csrf
                    },
                    success: (res) => {
                        // console.log(res)
                        if (res["fv"] == "formValidated") {
                            showAddresses()
                        } else {
                            handleEdit(oldRes);
                    
                        }
                    },

                    error: (err) => {
                        console.log(err)
                    },
                    processData: false,
                    contentType: false,
                    crossDomain: true,
                    // cache:false,
                    // processData: false
                })
            })
        }
            $.ajax({
            type: "POST",
            url: url,
            data: fd,
            headers: {
                "X-CSRFToken": csrf
            },
            success: (res) => {
                if (res["fv"]=="formValidated"){
                    showAddresses()
                }else{

                    handleEdit(res)
                }
            },

            error: (err) => {
                console.log(err)
            },
            processData: false,
            contentType: false,
            crossDomain: true,
            // cache:false,
            // processData: false
        })
        })
    })
}

function showAddresses() {
    $.get('http://127.0.0.1:8000/auth/credential/addresses'
    ).then(res => {
        let div = $(".ajx-div")

        div.html(res);
        $('html,body').animate({
        scrollTop:div.offset().top},
        'slow');

    })
}

function saveAddr(){
    let bt = document.getElementById("sve");
    let url = 'http://127.0.0.1:8000/orders/card/address/';
        let form = $('.a-u-a-f')
        let csrf = $("input[name=csrfmiddlewaretoken]").val();
        
        form.submit((e)=>{    
            e.preventDefault();

            let fd = new FormData(form[0]);
    
            function handleEdit(oldRes){
                $(".calit").html(oldRes);
                // let form = $(".a-u-a-f");
                    // console.log(form);
                // let csrf = $("input[name=csrfmiddlewaretoken]").val();
                    // console.log(csrf);
                // form.on("submit", (event)=> {
                form.submit((e)=>{    
                    e.preventDefault();    
                    let fd = new FormData(form[0])
                    $.ajax({
                        type: "POST",
                        url: url,
                        data: fd,
                        headers: {
                            "X-CSRFToken": csrf
                        },
                        success: (res) => {
                            // console.log(res)
                            if (res["code"]){
                    
                                $.get('http://127.0.0.1:8000/orders/paycheck/'+res["code"]).then(res=>{
                                    $(".calit").html(res);
                                })
                            } else {
                                // $(".form-cont-main").html(res);
                                // let form = $('.s-u-form')
                                // let csrf = $("input[name=csrfmiddlewaretoken]").val();
                                handleEdit(oldRes);
                                // aHan(form, csrf, url, ".form-cont-main", verF(res["id"]))

                            }
                        },

                        error: (err) => {
                            console.log(err)
                        },
                        processData: false,
                        contentType: false,
                        crossDomain: true,
                        // cache:false,
                        // processData: false
                    })
            })
        }
            $.ajax({
            type: "POST",
            url: url,
            data: fd,
            headers: {
                "X-CSRFToken": csrf
            },
            success: (res) => {
                if (res["code"]){
                    
                    $.get('http://127.0.0.1:8000/orders/paycheck/'+res["code"]).then(res=>{
                        $(".calit").html(res);
                                        
                        // if (history.pushState) {
                        //     window.history.pushState(null, "تاییدیه پرداخت", 'http://127.0.0.1:8000/orders/paycheck/'+res["code"]);
                        // } else {
                        //     window.history.replaceState(null, "تاییدیه پرداخت", 'http://127.0.0.1:8000/orders/paycheck/'+res["code"]);
                        //     // ** It seems that current browsers other than Safari don't support pushState
                        //     // title attribute. We can achieve the same thing by setting it in JS.
                        //     document.title = "تاییدیه پرداخت";
                        // }
                    })
                    

                }else{
                handleEdit(res)
                }
            },

            error: (err) => {
                console.log(err)
            },
            processData: false,
            contentType: false,
            crossDomain: true,
            // cache:false,
            // processData: false
        })
        })

}


function cAddress(){
    const url = 'http://127.0.0.1:8000/orders/card/address/'
    $.get(url).then(
        res => {
        $(".calit").html(res)
        // if (history.pushState) {
            // window.history.pushState(null, "آدرس ها", url);
        // } else {
            // window.history.replaceState(null, "آدرس ها", url);
            // ** It seems that current browsers other than Safari don't support pushState
            // title attribute. We can achieve the same thing by setting it in JS.
            // document.title = "آدرس ها";
        // }
        $('html,body').animate({
        scrollTop: $(".s-p-c").offset().top},
        'slow');
    })
}

function cCard(){

        $('html,body').animate({
        scrollTop: $(".s-p-c").offset().top},
        '');
        setTimeout(function() {
        window.location.reload();
            }, 300);

}

function sendAddress(){
    let btns = document.querySelectorAll(".ad-r-i")
    // let btns = $(".ad-r-i");
    // console.log(btns)
    let selectedCode;
    let csrf = $("input[name=csrfmiddlewaretoken]").val();
    // console.log(csrf)
    let btn = $("#a-c-btn")[0];
    for (const bt of btns){
        if (bt.checked){
            selectedCode = bt.value;
            // console.log(selectedCode)
            // brdomainName+eak;
        }
    }
    // btns.forEach(btn =>{
    //     if (btn.checked){
    //         selectedCode = btn.value;
    //         console.log(selectedCode)
    //     }
    // }
    // )
    if (selectedCode){
        let data = JSON.stringify({"code":encodeURIComponent(selectedCode)})
        
        let fd = new FormData()
        fd.append("code", selectedCode)
        // console.log(fd)
        $.ajax({
            type: "POST",
            url: 'http://127.0.0.1:8000/orders/card/address/',
            data: fd,
            headers: {
                "X-CSRFToken": csrf
            },
            success:(res)=>{
            //    console.log("success")
                // console.log(res)
                $(".calit").html(res);

            },
            error:(err)=>{
                console.log(err)
            },
            processData: false,
            contentType: false,
            crossDomain: true,
        })
        
        // async function postData(url = '', data) {
        //     // Default options are marked with *
        //     const response = await fetch(url, {
        //       method: 'POST', // *GET, POST, PUT, DELETE, etc.
        //       mode: 'same-origin', // no-cors, *cors, same-origin
        //       cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        //       credentials: 'same-origin', // include, *same-origin, omit
        //       headers: {
        //         'Content-Type': 'application/json',
        //         "X-CSRFToken": csrf
        //         // 'Content-Type': 'application/x-www-form-urlencoded',
        //       },
        //     //   redirect: 'follow', // manual, *follow, error
        //       referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        //       body: data, // body data type must match "Content-Type" header,
              
        //     });

        //     return response.json(); // parses JSON response into native JavaScript objects
        //   }
          
        //   postData('http://127.0.0.1:8000/orders/card/address/', {"code":311})
        //     .then((data) => {
        //       console.log(data); // JSON data parsed by `data.json()` call
        //     });
    }
        else
    {
        let form = $("#s-u-form");
    
        form.submit((e)=>{    
            e.preventDefault();   
        let fd = new FormData(form[0])
        // let uId = $("#uid").val();
        // console.log(uId)

        function handleSign(oldRes){
            $(".form-cont-main").html(oldRes);
            let form = $("#s-u-form");
                // console.log(form);
            let csrf = $("input[name=csrfmiddlewaretoken]").val();
                // console.log(csrf);
                form.submit((e)=>{    
                    e.preventDefault();   
                let fd = new FormData(form[0])
                $.ajax({
                    type: "POST",
                    url: url,
                    data: fd,
                    headers: {
                        "X-CSRFToken": csrf
                    },
                    success: (res) => {
                        console.log(res)
                        if (res["fv"] == "formValidated") {
                            verF(res["id"])
                        } else {
                            // $(".form-cont-main").html(res);
                            // let form = $('.s-u-form')
                            // let csrf = $("input[name=csrfmiddlewaretoken]").val();
                            handleSign(res);
                            // aHan(form, csrf, url, ".form-cont-main", verF(res["id"]))

                        }
                    },

                    error: (err) => {
                        console.log(err)
                    },
                    processData: false,
                    contentType: false,
                    crossDomain: true,
                    // cache:false,
                    // processData: false
                })
            })
        }
            $.ajax({
            type: "POST",
            url: url,
            data: fd,
                headers: {
                "X-CSRFToken": csrf
                },
            success: (res) => {
                // console.log(res)
                if (res["fv"]=="formValidated"){

                        verF(res["id"])
                }else{
                    // $(".form-cont-main").html(res);
                    // let form = $('.s-u-form')
                    // let csrf = $("input[name=csrfmiddlewaretoken]").val();
                    // aHan(form, csrf, url, ".form-cont-main", verF(res["id"]))
                    handleSign(res)
                }
            },

            error: (err) => {
                console.log(err)
            },
            processData: false,
            contentType: false,
            crossDomain: true,
            // cache:false,
            // processData: false
        })
            // handleSign()

    })
    }
    // console.log(btn)
}

// function aHan(form, csrf, url, container,sMes){
//     form.on("submit", (event) => {
//             event.preventDefault();
//         let fd = new FormData(form[0])
//         // console.log(fd)
//             $.ajax({
//                 method: "POST",
//                 url: url,
//                 data: fd,
//                 headers: {
//                     "X-CSRFToken": csrf
//                 },
//                 success: (res) => {
//                     if (res["fv"] == "formValidated") {
//                         if (typeof(sMes)  === "function"){
//                             sMes
//                         }else{
//                         $(".form-cont-main").html(sMes)
//                         }
//                     }
//                     else {
//                         $(container).html(res)
//                         let form = $("#s-u-form");
//                         let csrf = $("input[name=csrfmiddlewaretoken]").val();
//                         aHan(form, csrf, url, container, sMes)
//                     }
//                 },
//                 error:(err)=>{
//                     console.log(err)
//                 },
//             processData: false,
//             contentType: false,
//             crossDomain: true,
//             })
//
//         })
// }

function started(duration) {
    let start = Date.now();
    let intervalSetted = null;

    function timer() {
        let diff = duration - (((Date.now() - start) / 1000) | 0);
        let seconds = (diff % 60) | 0;
        seconds = seconds < 10 ? "0" + seconds : seconds;
        $('#resender').html("00:" + seconds);


        if (diff <= 0) {
            clearInterval(intervalSetted);
        }
    }

    timer();
    intervalSetted = setInterval(timer, 1000);
}

function createProgressbar(id, duration, callback) {
  // We select the div that we want to turn into a progressbar
  let progressbar = document.getElementById(id);
  progressbar.className = 'progressbar';

  // We create the div that changes width to show progress
  let progressbarinner = document.createElement('div');
  progressbarinner.className = 'inner';

  // Now we set the animation parameters
  progressbarinner.style.animationDuration = duration;

  // Eventually couple a callback
  if (typeof(callback) === 'function') {
    progressbarinner.addEventListener('animationend', callback);
  }

  // Append the progressbar to the main progressbardiv
  progressbar.appendChild(progressbarinner);

  // When everything is set up we start the animation
  progressbarinner.style.animationPlayState = 'running';
}

function verF(id) {
    let url =  'http://127.0.0.1:8000/auth/signup/v/' + id
    $.get(url
    ).then(res => {
        $(".form-cont-main").html(res);
        started(45);
        createProgressbar("progressbar", "45s", ()=>{
            let inner = $(".inner");
            let resender = $("#resender");
            let txt = $(".wait-txt");
            inner.attr("hidden", true)
            resender.text("ارسال مجدد کد");
            txt.text("")
        });
        let csrf = $("input[name=csrfmiddlewaretoken]").val();
        let form = $("#s-u-form");
        // console.log(form)
        form.submit((e)=>{    
            e.preventDefault();   
        let fd = new FormData(form[0])
        // console.log(fd)

            function handleV(oldRes){
            $(".form-cont-main").html(oldRes);
            // let form = $("#s-u-form");
                // console.log(form);
            // let csrf = $("input[name=csrfmiddlewaretoken]").val();
                // console.log(csrf);
            form.submit((e)=>{    
                e.preventDefault();   
                let fd = new FormData(form[0])
                $.ajax({
                    type: "POST",
                    url: url,
                    data: fd,
                    headers: {
                        "X-CSRFToken": csrf
                    },
                    success: (res) => {
                        // console.log(res)
                        if (res["fv"] == "formValidated") {
                            $(".form-cont-main").html("<div><span>حساب کاربری شما با موفقیت ثبت شد</span></div>")
                        } else {
                            // $(".form-cont-main").html(res);
                            // let form = $('.s-u-form')
                            // let csrf = $("input[name=csrfmiddlewaretoken]").val();
                            handleV(res);
                            // aHan(form, csrf, url, ".form-cont-main", verF(res["id"]))

                        }
                    },

                    error: (err) => {
                        console.log(err)
                    },
                    processData: false,
                    contentType: false,
                    crossDomain: true,
                    // cache:false,
                    // processData: false
                })
            })
        }
            $.ajax({
                type: "POST",
                url: url,
                data: fd,
                headers: {
                    "X-CSRFToken": csrf
                },
                success: (res) => {
                    if (res["fv"] == "formValidated") {
                        $(".form-cont-main").html("<div><span>حساب کاربری شما با موفقیت ثبت شد</span></div>")
                    }
                    else {
                        // $(".form-cont-main").html(res)
                        // let form = $("#s-u-form");
                        handleV(res)
                        // let csrf = $("input[name=csrfmiddlewaretoken]").val();
                        // aHan(form,csrf, id, url, ".form-cont-main", "<div><span>حساب کاربری شما با موفقیت ثبت شد</span></div>" )
                    }
                },
                error:(err)=>{
                    console.log(err)
                },
            processData: false,
            contentType: false,
            crossDomain: true,
            })

        })

    })
}

function signUp(){
    let url = 'http://127.0.0.1:8000/auth/signup/'
    $.get(url
    ).then(res => {
        $(".form-cont-main").html(res)

    let form = $("#s-u-form");
        // console.log(form);
    let csrf = $("input[name=csrfmiddlewaretoken]").val();
        // console.log(csrf);

    form.submit((e)=>{    
        e.preventDefault();   
        let fd = new FormData(form[0])
            // let uId = $("#uid").val();
            // console.log(uId)

        function handleSign(oldRes){
            $(".form-cont-main").html(oldRes);
            let form = $("#s-u-form");
                // console.log(form);
            let csrf = $("input[name=csrfmiddlewaretoken]").val();
                // console.log(csrf);
            form.submit((e)=>{    
                e.preventDefault();   
                let fd = new FormData(form[0])
                $.ajax({
                    type: "POST",
                    url: url,
                    data: fd,
                    headers: {
                        "X-CSRFToken": csrf
                    },
                    success: (res) => {
                        console.log(res)
                        if (res["fv"] == "formValidated") {
                            verF(res["id"])
                        } else {
                            // $(".form-cont-main").html(res);
                            // let form = $('.s-u-form')
                            // let csrf = $("input[name=csrfmiddlewaretoken]").val();
                            handleSign(res);
                            // aHan(form, csrf, url, ".form-cont-main", verF(res["id"]))

                        }
                    },

                    error: (err) => {
                        console.log(err)
                    },
                    processData: false,
                    contentType: false,
                    crossDomain: true,
                    // cache:false,
                    // processData: false
                })
            })
        }
            $.ajax({
            type: "POST",
            url: url,
            data: fd,
                headers: {
                "X-CSRFToken": csrf
                },
            success: (res) => {
                // console.log(res)
                if (res["fv"]=="formValidated"){

                        verF(res["id"])
                }else{
                    // $(".form-cont-main").html(res);
                    // let form = $('.s-u-form')
                    // let csrf = $("input[name=csrfmiddlewaretoken]").val();
                    // aHan(form, csrf, url, ".form-cont-main", verF(res["id"]))
                    handleSign(res)
                }
            },

            error: (err) => {
                console.log(err)
            },
            processData: false,
            contentType: false,
            crossDomain: true,
            // cache:false,
            // processData: false
        })
            // handleSign()

    })
    })
}

function payMethods(postalCode){
}

function checkPay(postalCode){
    let form = $("#checkpay");
    let url = "http://127.0.0.1:8000/orders/paycheck/"+postalCode;
    let csrf = $("input[name=csrfmiddlewaretoken]").val();
    let fd = new FormData(form[0]);
    function handleCheck(oldRes){
            $(".calit").html(oldRes);
            // let form = $("#checkpay");
                // console.log(form);
            // let csrf = $("input[name=csrfmiddlewaretoken]").val();
                // console.log(csrf);
            form.submit((e)=>{    
                e.preventDefault();   
                let fd = new FormData(form[0])
                $.ajax({
                    type: "POST",
                    url: url,
                    data: fd,
                    headers: {
                        "X-CSRFToken": csrf
                    },
                    success: (res) => {
                        // console.log(res)
                        if (res) {
                            console.log("sss")
                        } else {
                            // $(".form-cont-main").html(res);
                            // let form = $('.s-u-form')
                            // let csrf = $("input[name=csrfmiddlewaretoken]").val();
                            handleCheck(oldRes);
                            // aHan(form, csrf, url, ".form-cont-main", verF(res["id"]))

                        }
                    },

                    error: (err) => {
                        console.log(err)
                    },
                    processData: false,
                    contentType: false,
                    crossDomain: true,
                    // cache:false,
                    // processData: false
                })
            })
        }
            $.ajax({
            type: "POST",
            url: url,
            data: fd,
            headers: {
                "X-CSRFToken": csrf
            },
            success: (res) => {
                if (res["fv"]=="fnotnavalid"){
                    window.location.reload()
                }else{
                    top.location.href = res["link"]
                }
                
            },
            error: (err) => {
                console.log(err)
            },
            processData: false,
            contentType: false,
            crossDomain: true,
            // cache:false,
            // processData: false
        })

}

// function eAdr() {
//     let $myForm = $('.a-u-a-f')
//
//     $myForm.on("submit",(function (event) {
//         event.preventDefault()
//
//
//
//     }))
// }

function resendSms(){
    let inner = $(".inner");
    let resender = $("#resender");
    let txt = $(".wait-txt");
    // inner.attr("hidden", false)
    resender.text("");
    txt.text("ثانیه تا ارسال مجدد کد صبر کنید.");
    started(45);
    createProgressbar("progressbar", "45s",()=>{
        let inner = $(".inner");
        inner.attr("hidden", true);
        txt.text("");
        resender.text("ارسال مجدد کد");
    })
    $.get('http://127.0.0.1:8000/auth/signup/sres'
    ).then(res=>{
        $(".calit").html(res)
    });
}

function showOrders(){
      $.get('http://127.0.0.1:8000/auth/factor/pay'
    ).then(res=>{
        $(".ajx-div").html(res)
    });
}

function pPick(id){
    let changePot = $("#pcp"+id);
    if (changePot.is(":checked")){
            changePot.attr("checked", true)
            let soilStat = "True"
            console.log(soilStat)
    }else{
            changePot.removeAttr("checked")

            let soilStat = "False"
            console.log(soilStat)
        }
}

function soPick(id){
    let changeSoil = $("#pcs"+id);
    if (changeSoil.is(":checked")){
            changeSoil.attr("checked", true)
            let soilStat = "True"
            console.log(soilStat)
    }else{
            changeSoil.removeAttr("checked")
            let soilStat = "False"
            console.log(soilStat)
    }
}

function editOrder(id){
    let q = $("#pi"+id).val();
    let changeSoil = $("#pcs"+id);
    let changePot = $("#pcp"+id);
    let soilStat = "False";
    let potStat = "False";
    // console.log(changePot);
    // console.log(changeSoil);
    // console.log($(".pcp"+id).is(":checked"));
    if (changePot.is(":checked")){
            potStat = "True"
            console.log(potStat)
    }else{
            potStat = "False"
            console.log(potStat)
    }
    if (changeSoil.is(":checked")){
            soilStat = "True"
            console.log(soilStat)
    }else{
            soilStat = "False"
            console.log(soilStat)
    }

    console.log(soilStat)
    console.log(potStat)
    $.get('http://127.0.0.1:8000/auth/factor/pay/edit',{"oid":id, "qu":q, "soil":soilStat, "pot":potStat})
        .then(res=>{
            $(".btnad"+id).html("<div class='loader'></div>");
            setTimeout(()=>{
            $(".btnad"+id).html("<div class=\"f-f-p-s\" onclick=\"editOrder('{{p.id}}')\">\n" +
                "<div class=\"tick-div \" ><p class=\"tick-p\">✓</p></div>\n" +
                "</div>");
            location.reload();
            }, 1500);

    })
}

function editProfile(){
      $.get('http://127.0.0.1:8000/auth/profile/'
    ).then(res=>{
        $(".ajx-div").html(res);
          $('html,body').animate({
        scrollTop: $(".ajx-div").offset().top},
        'slow');
    });
}

function largeImg(imgSrc) {
    $("#main_img_l").attr("src", imgSrc);
}

// $("#cart-icon")[0].addEventListener("click", ()=>{
//     $("#results").attr("class", "results-active")
//     // console.log("gg")
// })

function dropDown(inp){
    // let divC = $(".dropdown-content-"+inp)
    let divC = document.getElementsByClassName("dropdown-content-"+inp)
    // $(".dropdown-content-"+inp).hasClass("d-d-d-d")? $(".dropdown-content-"+inp).removeClass("d-d-d-d"):$(".dropdown-content-"+inp).addClass("d-d-d-d")
    // $(".dropdown-content-"+inp).removeClass("d-d-d-c")
    let arr = [...divC]
    arr.forEach((div)=>{
        if (div.classList.contains("d-d-d-d")){
            // console.log("has dddd")
            
            div.setAttribute("closing", '');
            div.addEventListener("animationend", ()=>{
                div.classList.remove("d-d-d-d");
                div.classList.add("d-d-d-c");
                div.removeAttribute("closing");
            }, {once: true})
    

    }else{
        
        // console.log("has dddc")
        div.classList.remove("d-d-d-c")
        div.classList.add("d-d-d-d")
            
        }
    })
    

}
function slideUp(inp){
    $(".dropdown-content-"+inp).removeClass("d-d-d-d")

    $(".dropdown-content-"+inp).addClass("d-d-d-c")

}
//
// $(".b-p").first().addEventListener("onclick", hideCart)



function showCard(){
    let div = document.getElementById("results")
    // $(".results").toggleClass(["results-active"]);
    // console.log(document.getElementById("results").classList)
    if(div.classList.contains("results")){
        div.classList.remove("results");
        div.classList.add("results-active");
        
    }
    else{
        div.setAttribute("closing", '');
        div.addEventListener("animationend", (e)=>{
            div.classList.remove("results-active");
            div.classList.add("results");
            div.removeAttribute("closing");
        }, {once: true})
    }
    // console.log($(".results").classList())

    $.get('http://127.0.0.1:8000/orders/card/'
    ).then(res=>{
        $(".shop-item").html(res)
    })
    // function checkIt(){
    // if ($("#results").attr("class")=="results"){
    //     $("#results").attr("class", "results-active");
    //     console.log("attr re ast");
    //     $.get('http://127.0.0.1:8000/orders/card/'
    // ).then(res=>{
    //     $(".shop-item").html(res)
    // });
    // }else {
    //     console.log("attr re nist");
    //     $("#results").attr("class", "results");
    // }}

    // checkIt()

}


function hideCart(){
    // document.getElementById("results").classList.remove("results-active")
    
}


