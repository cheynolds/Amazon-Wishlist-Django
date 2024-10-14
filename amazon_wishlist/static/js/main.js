// Infinite Scroll and Go to Top Button functionality

$(document).ready(function () {
    let page = 1;
    let loading = false;  // Flag to prevent multiple simultaneous loads

    // Debounce function to prevent excessive scroll triggering
    function debounce(func, delay) {
        let debounceTimer;
        return function () {
            const context = this;
            const args = arguments;
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(() => func.apply(context, args), delay);
        };
    }

    // Function to load more products
    function loadMoreProducts() {
        if (!loading) {  // Prevent loading if already loading products
            loading = true;
            page += 1;  // Increment page number
            $('#loading').show();  // Show loading message

            $.ajax({
                url: '?page=' + page,
                type: 'GET',
                success: function (data) {
                    if (data.trim() !== '') {
                        $('#product-grid').append(data);
                        $('#loading').hide();
                        loading = false;  // Reset loading flag after success
                    } else {
                        $('#load-more-btn').hide();  // No more products
                        loading = false;
                    }
                },
                error: function () {
                    console.log('Failed to load more products');
                    $('#loading').hide();
                    loading = false;  // Reset loading flag after error
                }
            });
        }
    }

    // Debounced scroll event listener for infinite scrolling
    $(window).scroll(debounce(function () {
        if ($(window).scrollTop() + $(window).height() >= $(document).height() - 100) {
            loadMoreProducts();  // Load more when near the bottom
        }
    }, 200));  // Adjust the delay as needed

    // Load more products button (if needed)
    $('#load-more-btn').click(function () {
        loadMoreProducts();
    });

    // "Go to Top" Button functionality
    let goToTopBtn = document.getElementById("goToTopBtn");

    window.onscroll = function () {
        scrollFunction();
    };

    function scrollFunction() {
        if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
            goToTopBtn.style.display = "block";
        } else {
            goToTopBtn.style.display = "none";
        }
    }

    goToTopBtn.addEventListener("click", function () {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });
});

// main.js

function initializePriceHistoryChart(historyData) {
    console.log('Initializing chart with data:', historyData);  // Debugging

    const ctx = document.getElementById('priceHistoryChart').getContext('2d');
    
    const priceHistoryChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: historyData.dates,  // X-axis (dates)
            datasets: [{
                label: 'Price Over Time',
                data: historyData.prices,  // Y-axis (prices)
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 2,
                fill: false
            }]
        },
        options: {
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Date'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Price (USD)'
                    },
                    beginAtZero: false
                }
            }
        }
    });
}


// Export the function to make sure it's available globally
window.initializePriceHistoryChart = initializePriceHistoryChart;

