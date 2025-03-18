<?php
// order.php - Monolithic PHP API (No Microservices)
require_once 'db.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $customer_name = $_POST['customer_name'];
    $product_name = $_POST['product_name'];
    $price = $_POST['price'];

    $sql = "INSERT INTO orders (customer_name, product_name, price) VALUES (?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ssd", $customer_name, $product_name, $price);

    if ($stmt->execute()) {
        echo json_encode(["status" => "success", "order_id" => $conn->insert_id]);
    } else {
        echo json_encode(["status" => "error"]);
    }
}
?>
