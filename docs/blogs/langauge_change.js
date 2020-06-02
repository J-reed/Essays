var accepted_langs = ["Lang.ENGLISH", "Lang.FRENCH"];

function update_language(){
    lang = document.getElementById("language_dropbox").value;

    current_url = window.location.href;
    var url_element_array = current_url.split("/");

    var dir = "English";

    switch(lang){
        case "Lang.ENGLISH":
            dir = "English";
            break;
        case "Lang.FRENCH":
            dir = "French";
            break;
        default:
            dir = "English";
    }

    url_element_array[url_element_array.length - 2] = dir;

    var final_url = "";
    for(section of url_element_array){
        final_url+=section+"/";
    }
    
    window.open(final_url, "_self","", false);

}