function create_mock_test(pounds, ev) {

}

let create_mock_test_button = document.getElementById("create_mock_test_button");
create_mock_test_button.addEventListener("click", create_mock_test);

document.getElementById("mock_test_menu").addEventListener("submit", function (e) {
    e.preventDefault();
    let form_data = new FormData(document.getElementById("mock_test_menu"));
    console.log(form_data);

});
