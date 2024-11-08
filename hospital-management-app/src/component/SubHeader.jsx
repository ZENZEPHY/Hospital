import React from 'react'
import { Link } from 'react-router-dom'

const SubHeader = () => {
    return (
        <div>

            <nav class="navbar navbar-expand-lg bg-body-tertiary">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">HOSPITAL MANEGMENT APP</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav">

                            <Link class="nav-link active" aria-current="page" to="/view">Department</Link>
                            <Link class="nav-link" to="/ap">Appointments</Link>
                            <Link class="nav-link" to="/ba">Add Blood Donor</Link>
                            <Link class="nav-link" to="/">Login Out</Link>
                        </ul>
                    </div>
                </div>
            </nav>

        </div>
    )
}

export default SubHeader