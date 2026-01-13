function adjustPopoverPosition(popover) {
    const rect = popover.getBoundingClientRect();
    const viewportWidth = window.innerWidth;

    // If popover goes off the right
    if (rect.right > viewportWidth) {
        popover.style.left = 'auto';
        popover.style.right = '0';
        popover.style.transform = 'none';
    }

    // If popover goes off the left
    if (rect.left < 0) {
        popover.style.left = '0';
        popover.style.transform = 'none';
    }
}


document.addEventListener("DOMContentLoaded", () => {
    // Parse corrections JSON from template
    const corrections = JSON.parse(document.getElementById("corrections-data").textContent);

    // Find all popover triggers
    document.querySelectorAll(".popover-trigger").forEach(trigger => {
        const index = parseInt(trigger.dataset.correctionIndex, 10);
        const popover = trigger.querySelector(".popover");

        if (popover && corrections[index]) {
            popover.innerHTML = corrections[index].explanation;
        }

        // Toggle popover on click
        trigger.addEventListener("click", (event) => {
          event.stopPropagation();

          // Close others
          document.querySelectorAll(".popover").forEach(p => {
              if (p !== popover) p.style.display = "none";
          });

          // Toggle this one
          if (popover.style.display === "block") {
              popover.style.display = "none";
          } else {
              popover.style.display = "block";
              adjustPopoverPosition(popover); // <-- reposition if needed
          }

          // Re-render X posts inside this popover
          if (window.twttr && twttr.widgets) {
              twttr.widgets.load();
          }
      });
    });

    // Close popovers if clicking outside
    document.addEventListener("click", () => {
        document.querySelectorAll(".popover").forEach(p => {
            p.style.display = "none";
        });
    });
});
